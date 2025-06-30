import json
from optimizers.copilot_optimizer import CopilotOptimizer
from optimizers.replit_optimizer import ReplitOptimizer
from utils import analyze_prompt
from explain import generate_explanation

# Load tool configuration from JSON
# This function loads the rules for a specific tool from the tool_analysis.json file.
def load_tool_rules(tool_name):
    print(f"[LOG] Loading tool rules for: {tool_name}")  # Log for debugging
    with open("tool_analysis.json") as f:
        all_rules = json.load(f)
    return all_rules.get(tool_name, {})

# This function returns the appropriate optimizer class based on the tool name.
def get_tool_optimizer(tool_name, tool_rules):
    print(f"[LOG] Getting optimizer for tool: {tool_name}")  # Log for debugging
    if tool_name.lower() == "copilot":
        return CopilotOptimizer(tool_rules)
    elif tool_name.lower() == "replit":
        return ReplitOptimizer(tool_rules)
    return None

# This function displays the results to the user in a readable format.
def display_results(original, optimized, explanation):
    print("\n--- Original Prompt ---")
    print(original)
    print("\n--- Optimized Prompt ---")
    print(optimized)
    print("\n--- Explanation ---")
    print(explanation)

if __name__ == "__main__":
    print("Welcome to Adaptive Prompt Optimizer CLI")
    # Ask the user to enter their base prompt
    user_prompt = input("\nEnter your base prompt: ")
    # Ask the user to select the target tool
    tool_name = input("Select target tool (e.g., Copilot, Replit): ")

    print("[LOG] Analyzing prompt...")
    metadata = analyze_prompt(user_prompt)
    print(f"[LOG] Metadata extracted: {metadata}")
    rules = load_tool_rules(tool_name)
    print(f"[LOG] Tool rules loaded: {rules}")
    optimizer = get_tool_optimizer(tool_name, rules)

    if optimizer:
        print("[LOG] Optimizing prompt...")
        optimized_prompt = optimizer.optimize(user_prompt, metadata)
        print(f"[LOG] Optimized prompt: {optimized_prompt}")
        explanation = generate_explanation(user_prompt, optimized_prompt, tool_name)
        print(f"[LOG] Explanation generated: {explanation}")
        display_results(user_prompt, optimized_prompt, explanation)
    else:
        print("\nTool not supported yet.")