import gradio as gr
from controller import Controller

def build_gradio_ui(controller: Controller):
    edited_versions = []  

    def process_original(essay, task):
        suggested_edit = controller.run_workflow(essay, task, use_latest=False)  
        controller.accept_edit(suggested_edit) 
        edited_versions.append(suggested_edit)
        return suggested_edit, "\n\n---\n\n".join(edited_versions)  

    def process_latest(task):
        if controller.latest_edited_essay is None:
            return "No previous edits available", "\n\n---\n\n".join(edited_versions)
        suggested_edit = controller.run_workflow(controller.latest_edited_essay, task, use_latest=True)  
        controller.accept_edit(suggested_edit)  
        edited_versions.append(suggested_edit)
        return suggested_edit, "\n\n---\n\n".join(edited_versions)  

    with gr.Blocks() as demo:
        with gr.Tab("Essay Editor"):
            with gr.Row():
                essay_input = gr.Textbox(label="Insert your essay", lines=10, placeholder="Enter your essay here")
                tasks_input = gr.Textbox(label="Insert task", lines=2, placeholder="Enter your task here")

            with gr.Row():
                submit_essay_btn = gr.Button("Edit Original Essay")
                submit_draft_btn = gr.Button("Edit Latest Edited Essay", visible=False)

            with gr.Row():
                essay_output = gr.Textbox(label="Edited Essay", lines=10, interactive=False)
                history_output = gr.Textbox(
                    label="Edit History",
                    lines=15,
                    interactive=False,
                    placeholder="Previous edits will appear here"
                )

            
            submit_essay_btn.click(process_original, inputs=[essay_input, tasks_input], outputs=[essay_output, history_output])
            submit_draft_btn.click(process_latest, inputs=[tasks_input], outputs=[essay_output, history_output])

            essay_output.change(
                lambda new_value: (
                    new_value,
                    gr.update(visible=True)  
                ),
                inputs=[essay_output],
                outputs=[essay_output, submit_draft_btn]  
            )

    return demo
