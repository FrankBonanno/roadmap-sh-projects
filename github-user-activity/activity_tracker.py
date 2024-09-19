import time
import requests
import argparse

def fetch_activity(username, token=None):
  url = f"https://api.github.com/users/{username}/events"
  headers = {'User-Agent': 'Github-Activity-Tracker'}

  if token:
    headers['Authorization'] = f"token {token}"
    print(f" -> Using personal access token for authentication ...")

  start_time = time.time()  # Start the timer for measuring response time
  response = requests.get(url, headers=headers)
  end_time = time.time()  # End the timer

  # Show rate limit information
  if 'X-RateLimit-Limit' in response.headers:
    print(f" -> Rate Limit: {response.headers['X-RateLimit-Limit']} requests per hour")
  if 'X-RateLimit-Remaining' in response.headers:
    print(f" -> Remaining Requests: {response.headers['X-RateLimit-Remaining']}")
  if 'X-RateLimit-Reset' in response.headers:
    reset_time = int(response.headers['X-RateLimit-Reset'])
    reset_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reset_time))
    print(f" -> Rate Limit Resets At: {reset_timestamp}")
  
  # Show GitHub API version
  if 'X-GitHub-Media-Type' in response.headers:
    print(f" -> GitHub API Version: {response.headers['X-GitHub-Media-Type']}")
  
  # Show response time (latency)
  response_time = end_time - start_time
  print(f" -> Response Time: {response_time:.2f} seconds")

  # Check for rate limit exceeded
  if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
    if response.headers['X-RateLimit-Remaining'] == '0':
      print(f"Rate limit exceeded. Try again later.")
      return None

  # Check for other errors
  if response.status_code != 200:
    print(f"Error fetching activity for {username}. Status code: {response.status_code}")
    return None

  return response.json()

def format_event(event):
  event_type = event['type']
  repo_name = event['repo']['name']
  event_time = event['created_at']

  # print(f"Event type: {event_type}, Repo: {repo_name}")

  if event_type == 'PushEvent':
    num_commits = len(event['payload']['commits'])
    return f"- {event_time}: Pushed {num_commits} commits to {repo_name}"

  elif event_type == 'IssuesEvent':
    action = event['payload']['action']
    return f"- {event_time}: {action.capitalize()} a new issue in {repo_name}"

  elif event_type == 'WatchEvent':
    return f"- {event_time}: Starred {repo_name}"

  elif event_type == 'ForkEvent':
    return f"- {event_time}: Forked {repo_name} from {event['payload']['forkee']['full_name']}"
  
  elif event_type == 'PullRequestEvent':
    action = event['payload']['action']
    return f"- {event_time}: {action.capitalize()} a pull request in {repo_name}"
  
  elif event_type == 'PublicEvent':
    return f"- {event_time}: Made {repo_name} public"
  
  elif event_type == 'CreateEvent':
    ref_type = event['payload']['ref_type']
    ref = event['payload']['ref'] or repo_name  # ref could be the repo, branch, or tag
    return f"- {event_time}: Created {ref_type} '{ref}' in {repo_name}"
  
  elif event_type == 'DeleteEvent':
    ref_type = event['payload']['ref_type']
    ref = event['payload']['ref']
    return f"- {event_time}: Deleted {ref_type} '{ref}' in {repo_name}"
  
  elif event_type == 'PullRequestReviewEvent':
    action = event['payload']['action']
    return f"- {event_time}: {action.capitalize()} a pull request review in {repo_name}"
  
  elif event_type == 'IssueCommentEvent':
    action = event['payload']['action']
    return f"- {event_time}: {action.capitalize()} an issue comment in {repo_name}"
  
  elif event_type == 'MemberEvent':
    action = event['payload']['action']
    member = event['payload']['member']['login']
    return f"- {event_time}: {action.capitalize()} {member} as a collaborator in {repo_name}"

  return f"- {event_time}: Performed an unknown event in {repo_name}"

def main():
  # Create the argument parser
  parser = argparse.ArgumentParser(description="Fetch GitHub activity for a given user in the last 90 days.")
  parser.add_argument('username', type=str, help="GitHub username to fetch activity for.")
  parser.add_argument('--token', type=str, help="GitHub personal access token for authentication.")
  args = parser.parse_args()

  username = args.username
  token = args.token  # Get the token from the command-line argument

  print(f"Fetching recent activity for <{username}> ...")

  # Pass the token to the fetch_activity function
  events = fetch_activity(username, token)

  # Print Break Line
  print("-" * 50)

  if events:
    for event in events[:10]:  # Show the first 10 events
      formatted_event = format_event(event)
      print(formatted_event)
  else:
    print(f"No recent activity found for {username}.")

if __name__ == "__main__":
  main()