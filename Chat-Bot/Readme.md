

---

### **Assignment 01: Understanding OpenAI Chat Completion API Parameters**
#### **Objective:**
To understand and explain the functionality of specific parameters used in the OpenAI Chat Completion API.

---

### **Explanations of Parameters**

#### **1. Messages**
- **Purpose**:  
  This parameter represents the conversation between the user and the AI. It includes both user inputs (prompts) and AI responses. 
- **Structure**:  
  Messages are passed as an array of objects, where each object contains:
  - `role`: Defines who is speaking (`system`, `user`, or `assistant`).
  - `content`: The text content of the message.
- **Example**:
  ```json
  [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI stands for Artificial Intelligence."}
  ]
  ```
  This structure ensures a conversational context.

---

#### **2. Model**
- **Purpose**:  
  Specifies which OpenAI model will process the request. Different models vary in capabilities, speed, and cost (e.g., `gpt-3.5-turbo`, `gpt-4`).
- **Example**:  
  Using `gpt-3.5-turbo` is cost-efficient for quick responses, while `gpt-4` offers deeper reasoning.

---

#### **3. Max Completion Tokens**
- **Purpose**:  
  Defines the maximum number of tokens (words, parts of words, or punctuation) the model can generate in a single response.
- **Why It Matters**:  
  - A higher token limit allows for longer outputs.
  - Must be within the model's total token limit (input + output).
- **Example**:
  If you set `max_tokens` to 100, the response will not exceed 100 tokens.

---

#### **4. n**
- **Purpose**:  
  Specifies the number of responses you want the API to generate for a single prompt.
- **Example**:
  - Setting `n: 3` generates three different responses for the same prompt.
  - Useful for exploring multiple options or styles of response.

---

#### **5. Stream**
- **Purpose**:  
  Enables token-by-token streaming of the model's response, providing real-time output as it is generated.
- **Use Case**:  
  - Ideal for chat applications where immediate feedback is required.
- **Example**:  
  Watching a response build like a typing effect.

---

#### **6. Temperature**
- **Purpose**:  
  Controls the randomness of the output.  
  - Higher values (e.g., `0.8`) make responses more creative.  
  - Lower values (e.g., `0.2`) make responses more deterministic and focused.
- **Example**:
  - Temperature = 1.0: "AI is an exciting field with many possibilities!"  
  - Temperature = 0.2: "AI stands for Artificial Intelligence."

---

#### **7. Top_p**
- **Purpose**:  
  Another way to control randomness by using nucleus sampling.  
  - It limits the output to the smallest set of tokens with a cumulative probability of `p`.
- **How It Works**:
  - `Top_p = 0.9`: The model considers only the top 90% of possible words for each response.
  - It works well with `temperature` for fine-tuning output randomness.

---

#### **8. Tools**
- **Purpose**:  
  Refers to external APIs or plugins integrated with the model, expanding its functionality.
- **Example**:
  Tools might allow the model to fetch data from a web source, perform calculations, or retrieve specific files.

---

### **How Parameters Work Together**
These parameters are interconnected:
- **`Temperature` and `Top_p`**: Fine-tune the randomness together. Use either or both for specific styles.  
- **`Messages` and `Model`**: Provide context and control the capabilities of the conversation.  
- **`n`**: Enables experimentation by generating multiple responses.  

### **Tips for Submission**
1. ![alt text](<SS/Screenshot 2024-12-13 211106.png>)
2. ![alt text](<SS/Screenshot 2024-12-13 211153.png>)
3. ![alt text](<SS/Screenshot 2024-12-13 211251.png>)
4. ![alt text](<SS/Screenshot 2024-12-13 211355.png>)
## Google Colab code by Chat bot 
5. ![alt text](<SS/Screenshot 2024-12-13 212258.png>)
6. ![alt text](<SS/Screenshot 2024-12-13 212416.png>)

---





