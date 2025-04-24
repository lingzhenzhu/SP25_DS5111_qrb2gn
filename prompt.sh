#!/bin/bash

PROMPT="$1"
MAX_TOKENS="$2"

# Escape double quotes inside the prompt
#ESCAPED_PROMPT=$(echo "$PROMPT" | sed 's/"/\\"/g')

curl -X POST "http://localhost:8080/v1/completions" \
     -H "Content-Type: application/json" \
     -d "{
          \"prompt\": \"$PROMPT\",
          \"max_tokens\": $MAX_TOKENS
         }"
