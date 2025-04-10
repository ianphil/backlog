import click
from backlog.core.markdown import write_markdown_file
from backlog.core.storage import load_tasks, save_tasks
from backlog.core.task_ops import add_task, filter_tasks

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

@task.command("list")
@click.option("--status", type=click.Choice(["pending", "done", "deferred"]), 
              help="Filter tasks by status")
@click.option("--priority", type=click.Choice(["low", "medium", "high"]), 
              help="Filter tasks by priority")
def list_tasks(status, priority):
    """List tasks in your backlog with optional filtering"""
    task_collection = load_tasks()
    
    # Apply filters if provided
    filtered_tasks = filter_tasks(task_collection.tasks, status, priority)
    
    if not filtered_tasks:
        click.echo("📝 No tasks found matching the criteria")
        return
    
    # Display header with filter info
    filter_info = []
    if status:
        filter_info.append(f"status={status}")
    if priority:
        filter_info.append(f"priority={priority}")
    
    filter_text = f" (filtered by: {', '.join(filter_info)})" if filter_info else ""
    click.echo(f"📋 Task List{filter_text}:")
    
    # Display the tasks in a table-like format
    for task in filtered_tasks:
        status_emoji = {
            "pending": "⏳",
            "done": "✅",
            "deferred": "⏱️"
        }.get(task.status, "⏳")
        
        priority_marker = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🔵"
        }.get(task.priority, "⚪")
        
        click.echo(f"{status_emoji} [{task.id}] {priority_marker} {task.title}")