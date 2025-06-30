# This module provides utility functions for prompt analysis.
def analyze_prompt(prompt):
    # metadata will store information about the prompt
    metadata = {}

    print(f"[LOG] Analyzing prompt: {prompt}")
    # Check if the prompt mentions a programming language (Python, HTML, JS, JavaScript)
    if any(lang in prompt.lower() for lang in ["python", "html", "js", "javascript"]):
        metadata["language"] = True
        print("[LOG] Detected language in prompt.")
    else:
        metadata["language"] = False
        print("[LOG] No language detected in prompt.")

    # Check if the prompt is vague (less than 8 words or contains 'app')
    metadata["is_vague"] = len(prompt.split()) < 8 or "app" in prompt.lower()
    print(f"[LOG] Vague prompt: {metadata['is_vague']}")

    return metadata
