## ✅ **Planned CLI Commands**

### 🗂 **Task Commands**
- [x] `backlog task add --title "..." --description "..." --priority high`
- [ ] `backlog task remove <id> [--force]`
- [ ] `backlog task update <id> --status done`
- [ ] `backlog task list [--status pending|done|deferred] [--priority high|medium|low]`
- [ ] `backlog task show <id>`
- [ ] `backlog task generate-md <id>`

---

### 🧩 **Subtask Commands**
- [ ] `backlog subtask add <parent_id> --title "..." --description "..." --acceptance "..."`
- [ ] `backlog subtask update <parent_id>.<sub_id> --status done`
- [ ] `backlog subtask list <parent_id>`

---

### 🤖 **AI Integration**
- [ ] `backlog ai parse-prd <path_to_prd.md>`
- [ ] `backlog ai expand <task_id> [--num-subtasks 3]`
- [ ] `backlog ai rewrite <task_id> --context "..."`

---

### 🛠 **Meta / Utility**
- [ ] `backlog init --project "MyProject"`
- [ ] `backlog status`
- [ ] `backlog version`
- [ ] `backlog help`
