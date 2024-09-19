import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest='action', help='Action to perform')

    # 'add' command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Description of the task to add')

    # 'update' command
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', help='ID of the task to update')
    update_parser.add_argument('description', help='New description for the task')

    # 'delete' command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help='ID of the task to delete')

    # 'list' command with an optional positional 'status' argument
    list_parser = subparsers.add_parser('list', help='List all tasks or filter by status')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], help='Filter tasks by status')

    # 'mark-in-progress' command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in progress')
    mark_in_progress_parser.add_argument('id', help='ID of the task to mark as in progress')

    # 'mark-done' command
    mark_done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    mark_done_parser.add_argument('id', help='ID of the task to mark as done')

    return parser