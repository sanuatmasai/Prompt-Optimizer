from optimizers.base_optimizer import BaseOptimizer

# This class optimizes prompts specifically for Replit
class ReplitOptimizer(BaseOptimizer):
    def optimize(self, prompt, metadata):
        print("[LOG] ReplitOptimizer: Starting optimization...")
        # If no language is detected, add a project creation hint for Replit
        if not metadata.get("language"):
            print("[LOG] No language detected. Adding Replit project creation hint.")
            prompt = "Create a project in Replit using Python. " + prompt

        # If prompt is vague, add a request for file structure and code snippets
        if metadata.get("is_vague"):
            print("[LOG] Prompt is vague. Adding request for file structure and code snippets.")
            prompt += "\nInclude file structure and code snippets."

        print(f"[LOG] ReplitOptimizer: Final optimized prompt: {prompt}")
        return prompt
