print("Testing imports...")
try:
    import pandas as pd
    print("Pandas imported successfully")
    import numpy as np
    print("NumPy imported successfully")
    from sklearn.ensemble import RandomForestClassifier
    print("Scikit-learn imported successfully")
except Exception as e:
    print(f"Error: {str(e)}")

print("Test completed") 