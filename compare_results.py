#!/usr/bin/env python3
"""
Compare original results with newly generated results to verify consistency.
"""

import pandas as pd
import sys
from pathlib import Path

def compare_results(original_file, new_file):
    """Compare two result CSV files."""
    print(f"\n{'='*80}")
    print(f"Comparing: {original_file.name}")
    print(f"{'='*80}")
    
    # Read both files
    try:
        df_original = pd.read_csv(original_file)
        df_new = pd.read_csv(new_file)
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        return False
    
    # Check dimensions
    print(f"\n📊 Dimensions:")
    print(f"  Original: {df_original.shape}")
    print(f"  New:      {df_new.shape}")
    
    if df_original.shape != df_new.shape:
        print(f"  ⚠️  Different dimensions!")
    else:
        print(f"  ✅ Same dimensions")
    
    # Check columns
    print(f"\n📋 Columns:")
    original_cols = set(df_original.columns)
    new_cols = set(df_new.columns)
    
    if original_cols == new_cols:
        print(f"  ✅ Same columns ({len(original_cols)} columns)")
    else:
        print(f"  ⚠️  Different columns!")
        if original_cols - new_cols:
            print(f"  Missing in new: {original_cols - new_cols}")
        if new_cols - original_cols:
            print(f"  Extra in new: {new_cols - original_cols}")
    
    # Compare diagnosis accuracy (if applicable)
    if 'diagnosis' in df_original.columns and 'actual_diagnosis' in df_original.columns:
        print(f"\n🎯 Diagnosis Accuracy:")
        
        # Original accuracy
        original_correct = (df_original['diagnosis'] == df_original['actual_diagnosis']).sum()
        original_accuracy = original_correct / len(df_original) * 100
        
        # New accuracy
        new_correct = (df_new['diagnosis'] == df_new['actual_diagnosis']).sum()
        new_accuracy = new_correct / len(df_new) * 100
        
        print(f"  Original: {original_correct}/{len(df_original)} = {original_accuracy:.2f}%")
        print(f"  New:      {new_correct}/{len(df_new)} = {new_accuracy:.2f}%")
        
        diff = abs(original_accuracy - new_accuracy)
        if diff < 1.0:
            print(f"  ✅ Very similar accuracy (diff: {diff:.2f}%)")
        elif diff < 5.0:
            print(f"  ⚠️  Slightly different accuracy (diff: {diff:.2f}%)")
        else:
            print(f"  ❌ Significantly different accuracy (diff: {diff:.2f}%)")
    
    # Sample comparison
    print(f"\n🔍 Sample Comparison (first 3 rows):")
    if 'diagnosis' in df_original.columns:
        print("\nOriginal diagnoses:")
        print(df_original['diagnosis'].head(3).to_list())
        print("\nNew diagnoses:")
        print(df_new['diagnosis'].head(3).to_list())
    
    return True

def main():
    """Main comparison function."""
    original_dir = Path("results_original")
    new_dir = Path("results")
    
    print("\n" + "="*80)
    print("RESULTS COMPARISON TOOL")
    print("="*80)
    
    # Find all CSV files in original results
    subdirs = ['agent_wkb', 'agent_kb', 'two_agent_kb']
    
    for subdir in subdirs:
        original_subdir = original_dir / subdir
        new_subdir = new_dir / subdir
        
        if not original_subdir.exists():
            continue
        
        print(f"\n\n{'#'*80}")
        print(f"# {subdir.upper()}")
        print(f"{'#'*80}")
        
        # Get all CSV files
        csv_files = list(original_subdir.glob("*.csv"))
        
        for original_file in csv_files:
            # Skip cleaned files
            if "_cleaned" in original_file.name:
                continue
            
            new_file = new_subdir / original_file.name
            
            if new_file.exists():
                compare_results(original_file, new_file)
            else:
                print(f"\n⏳ {original_file.name}: New results not yet generated")
    
    print("\n" + "="*80)
    print("Comparison complete!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
