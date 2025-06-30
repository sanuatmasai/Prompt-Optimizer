from optimizers.base_optimizer import BaseOptimizer

# This class optimizes prompts specifically for GitHub Copilot
class CopilotOptimizer(BaseOptimizer):
    def optimize(self, prompt, metadata):
        print("[LOG] CopilotOptimizer: Starting optimization...")
        # Example logic: Add language hint if not present
        if not metadata.get("language"):
            print("[LOG] No language detected. Adding language hint to prompt.")
            prompt = "In Python, " + prompt

        # If vague, add clarity
        if metadata.get("is_vague"):
            print("[LOG] Prompt is vague. Adding request for input/output examples.")
            prompt += "\nInclude input/output examples."

        print(f"[LOG] CopilotOptimizer: Final optimized prompt: {prompt}")
        return prompt
