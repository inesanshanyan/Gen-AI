

PLAN_EDITS_PROMPT = """Your task is to analyze the essay and understand the given task, which specifies the required edits.
You must plan the edits strictly according to the task instructions. If a change is not mentioned, do not include it in the plan."""

EDITOR_PROMPT = """You are an essay editor. Given an edit plan and a draft, apply only the specified changes."""

CRITIQUE_PROMPT = """You will receive a task, the original essay, and an edited draft. Your task is to compare the draft with the original essay and give a feedback whether the edits successfully fulfill the task requirements. Provide constructive feedback on necessary improvements."""

REFLECT_PROMPT = """You will receive a critique, an edit plan, and a draft. Revise the draft based on the critique and edit plan, ensuring all mentioned issues are addressed.
Do not modify any parts that are not mentioned in the critique. Don't add your instructions to the draft, the draft should be strictly according to the task, including only the edited essay."""