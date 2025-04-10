import click
from backlog.core.markdown import write_markdown_file
from backlog.core.storage import load_tasks, save_tasks
from backlog.core.task_ops import add_task

@click.group()
def cli():
    """Backlog - AI-Directed Task Backlog Manager"""
    pass

@cli.group()
def task():
    """Manage tasks in your backlog"""
    pass


@task.command("add")
@click.option("--title", prompt="Task title", help="Short task title")
@click.option("--description", prompt="Description", help="What’s this task about?")
@click.option("--priority", default="medium", type=click.Choice(["low", "medium", "high"]), help="Task priority")
def add(title, description, priority):
    """Add a new task to your backlog"""
    tasks = load_tasks()

    # Basic validation
    if not title.strip():
        click.echo("❌ Title cannot be empty.")
        return

    task = add_task(title, description, priority, tasks)
    save_tasks(tasks)
    md_path = write_markdown_file(task)

    click.echo(f"✅ Task [{task.id}] added: {task.title}")
    click.echo(f"📄 Markdown: {md_path}")
