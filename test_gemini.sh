#!/bin/bash

# Quick test script using Google Gemini models only
# Tests a subset to verify the system works before full run

echo "========================================="
echo "Quick Test: Gemini Models"
echo "========================================="

# Activate virtual environment
source venv/bin/activate

echo ""
echo "Test 1: Agent WITHOUT Knowledge Base (gemini-2.0-flash)"
echo "---------------------------------------------------------"
python scripts/agent_without_kb.py \
    --provider GOOGLE \
    --model gemini-2.0-flash \
    --results_dir results/agent_wkb

echo ""
echo "Test 2: Agent WITH Knowledge Base (gemini-2.0-flash)"
echo "-----------------------------------------------------"
python scripts/one_agent_with_kb.py \
    --provider GOOGLE \
    --model gemini-2.0-flash \
    --results_dir results/agent_kb

echo ""
echo "========================================="
echo "Tests Complete!"
echo "========================================="
echo ""
echo "Running comparison..."
python compare_results.py
