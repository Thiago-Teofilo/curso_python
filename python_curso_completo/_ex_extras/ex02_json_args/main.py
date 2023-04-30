from argparse import ArgumentParser
from taskList import TaskList
from pathlib import Path

parser = ArgumentParser()

parser.add_argument(
    '-a', '--add',
    help='Add item on list task',
    type=str,
    nargs='+',
    required=False
    )
parser.add_argument(
    '-c', '--confirm',
    help='Mark confirm item on list task',
    action='store_true'
)
parser.add_argument(
    '-s', '--show',
    help='Show list task',
    action='store_true'
)
parser.add_argument(
    '-r', '--remove',
    help='Remove item on list task',
    type=str,
    nargs='+',
    required=False
)

LOCAL_JSON = Path(__file__).parent / 'task_list.json'

args = parser.parse_args()

taskList = TaskList(local_json=LOCAL_JSON)

if args.add is not None:
    taskList.add(args.add)

if args.show:
    taskList.show()

if args.remove is not None:
    taskList.remove(args.remove[0])

taskList.save(local_json=LOCAL_JSON)