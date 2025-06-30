# This is the base class for all optimizers. Each tool-specific optimizer should inherit from this class.
class BaseOptimizer:
    def __init__(self, tool_rules):
        # Store the rules for the tool (from tool_analysis.json)
        self.tool_rules = tool_rules
        print(f"[LOG] BaseOptimizer initialized with rules: {tool_rules}")

    # This method should be implemented by subclasses to optimize prompts
    def optimize(self, prompt, metadata):
        raise NotImplementedError("Subclasses should implement this!")