## ✅ CLI Command Set (Initial Spec)
<spec>
These are atomic and composable—just enough to start, and easy to expand.

### **Task Commands**
```
backlog task add --title "Title" --description "..." --priority high
backlog task remove <id> [--force]
backlog task update <id> --status done
backlog task list [--status pending|done|deferred] [--priority high|medium|low]
backlog task show <id>
backlog task generate-md <id>
```

### **Subtask Commands**
```
backlog subtask add <parent_id> --title "..." --description "..." --acceptance "..."
backlog subtask update <parent_id>.<sub_id> --status done
backlog subtask list <parent_id>
```

### **AI Integration**
```
backlog ai parse-prd <path_to_prd.md>
backlog ai expand <task_id> [--num-subtasks 3]
backlog ai rewrite <task_id> --context "..."
```

### **Meta/Utility**
```
backlog init --project "MyProject"
backlog status
backlog version
backlog help
```

---

## 🧠 Architecture Breakdown

We'll look at this from both the **Atomic Composable** angle (think: plug-and-play functions) and **Vertical Slice** angle (feature-oriented layering).

---

### 🔧 Atomic Composable Architecture

Each core unit is a function or module that does one thing well and is independently testable:

- `load_tasks() / save_tasks()` – handles reading/writing `tasks.json`
- `parse_markdown_task(file_path)` – generates JSON from `.md`
- `generate_markdown(task_obj)` – emits `.md` from JSON
- `add_task(data)`, `update_task(id, updates)`, `remove_task(id)`
- `validate_task(task_obj)` – using something like Pydantic
- `openai_prompt(template, context)` – general-purpose prompt executor
- `expand_task_to_subtasks(task_obj, context)` – wrapper around AI generation
- `resolve_dependencies(task_list)` – builds dependency graph
- `format_output(data, style='json'|'table'|'pretty')`

These get composed into CLI actions or batch jobs.

---

### 🏗 Vertical Slice Architecture

Each vertical slice delivers a complete end-to-end feature, from CLI down to file system and AI:

---

#### 1. **Add Task Slice**
- **CLI**: `task add`
- **App Logic**: parse args → validate → update JSON → write file
- **Storage**: Update `tasks.json`, optionally create `.md`
- **Reusable units**: `add_task`, `save_tasks`, `generate_markdown`

---

#### 2. **List Tasks Slice**
- **CLI**: `task list [--filters]`
- **Logic**: Load JSON → filter → format
- **Units**: `load_tasks`, `filter_tasks`, `format_output`

---

#### 3. **AI PRD Parsing Slice**
- **CLI**: `ai parse-prd`
- **Flow**: Read `.md` → send to OpenAI → receive tasks → validate/add to `tasks.json`
- **Units**: `openai_prompt`, `validate_task`, `add_task`, `save_tasks`

---

#### 4. **Expand Task to Subtasks Slice**
- **CLI**: `ai expand`
- **Flow**: Fetch task → send to AI → validate subtasks → add to `tasks.json`
- **Units**: `expand_task_to_subtasks`, `add_subtask`, `save_tasks`

---

#### 5. **Task Markdown Sync Slice**
- **CLI**: `generate-md <id>`
- **Flow**: Get task → render markdown → write file
- **Units**: `generate_markdown`, `write_file`

---

So you’ve got:

- **Atomic modules**: plug-and-play building blocks
- **Vertical slices**: fully working features for real use cases
<\ spec>