
# Tool Calling
```
LLM decides what tool is needed, the application executes the tool, the result goes back to the LLM, and the LLM uses that result to continue or produce the final answer.
```

## 1. What is Tool Calling?

Tool Calling is a mechanism that allows an LLM to **request an external function/tool** when it needs some capability that is not available through its own knowledge or reasoning.

                    USER
                      |
                      v
                User Question
                      |
                      v
                     LLM
                      |
             Does it need a tool?
                 /          \
               No            Yes
               |              |
               v              v
         Final Answer      Tool Call
                              |
                              v
                       Application
                              |
                              v
                       Execute Tool
                              |
                              v
                        Tool Result
                              |
                              v
                             LLM
                              |
                    Does it need another
                           tool?
                       /           \
                     Yes            No
                      |              |
                      v              v
                  Tool Call    Final Answer



                  # Tool Calling

## 1. What is Tool Calling?

Tool Calling is a mechanism that allows an LLM to **request an external tool/function** when it needs a capability that it cannot reliably perform by itself.

A tool can be:

- A Python function
- An API
- A database query
- A web search
- A calculator
- A file/document search
- An external service

### Example

```text
User:
What is the price of iPhone 17?

LLM:
Tool Call → get_product_price("iPhone 17")

Application:
Executes get_product_price("iPhone 17")

Tool:
Returns → 1000

Application:
Sends 1000 back to the LLM

LLM:
Final Answer → iPhone 17 costs ₹1000.
```

---

# 2. When Should We Use a Tool?

Use a tool when the LLM needs something **outside of its own response generation**.

Common situations:

| Requirement | Tool Example |
|---|---|
| Current/external information | `get_weather()` |
| Product information | `get_product_price()` |
| Accurate calculation | `calculator()` |
| Database information | `query_database()` |
| Web search | `web_search()` |
| Document search | `search_documents()` |
| Send an email | `send_email()` |
| Create an order | `create_order()` |
| Get stock price | `get_stock_price()` |

### Simple Rule

> **If the task requires external data, accurate computation, or an external action, a tool may be required.**

---

# 3. How Does the LLM Know That a Tool Exists?

The application provides the LLM with **tool definitions**.

For example:

```text
Tool: get_product_price

Description:
Returns the price of a product.

Parameter:
product: string
```

And:

```text
Tool: calculator

Description:
Performs mathematical calculations.

Parameter:
expression: string
```

The LLM receives:

```text
User Request
+
Available Tool Definitions
```

The LLM then decides whether one of the available tools can help.

---

# 4. Who Decides Whether to Call a Tool?

## The LLM decides.

The application gives the LLM:

```text
User Request
+
Available Tools
```

The LLM analyzes the request and decides:

```text
Do I need a tool?

        ↓

     YES / NO
```

### If NO:

```text
LLM → Final Answer
```

### If YES:

```text
LLM → Tool Call
```

So the basic idea is:

```text
LLM = Decides which tool is needed

Application = Executes the selected tool
```

---

# 5. How Does the LLM Know Which Tool to Call?

The LLM compares the **user's intent** with the **tool descriptions/capabilities**.

### Example

User:

```text
What is the price of iPhone 17?
```

Available tools:

```text
get_product_price(product)
calculator(expression)
```

The LLM understands:

```text
User wants:
Product price

Available tool:
get_product_price()

Therefore:
Call get_product_price()
```

It generates:

```text
get_product_price("iPhone 17")
```

---

### Another Example

User:

```text
Calculate 5000 - 1000.
```

The LLM understands:

```text
User wants:
Mathematical calculation

Available tool:
calculator()

Therefore:
Call calculator()
```

It generates:

```text
calculator("5000 - 1000")
```

---

# 6. Does Every Question Require a Tool?

## No.

If the LLM can answer the question without external information or action, it can answer directly.

Example:

```text
User:
What is JavaScript?
```

The LLM can simply answer:

```text
JavaScript is a programming language...
```

No tool is required.

But:

```text
User:
What is the current price of Bitcoin?
```

A real-time data tool may be required:

```text
get_crypto_price("Bitcoin")
```

---

# 7. What Exactly Is a Tool Call?

A **Tool Call** is a structured request from the LLM that tells the application:

1. Which tool should be executed?
2. What arguments should be passed to that tool?

Conceptually:

```text
Tool Call = Tool Name + Arguments
```

Example:

```text
get_product_price("iPhone 17")
```

Here:

```text
Tool Name:
get_product_price

Argument:
"iPhone 17"
```

Another example:

```text
calculator("5000 - 1000")
```

Here:

```text
Tool Name:
calculator

Argument:
"5000 - 1000"
```

---

# 8. Who Actually Executes the Tool?

## The application executes the tool.

The LLM does **not** execute the Python function itself.

For example, the LLM may generate:

```text
get_product_price("iPhone 17")
```

But the LLM does not directly run:

```python
get_product_price("iPhone 17")
```

Your Python application receives the tool call and executes the function:

```python
tool = tools[tool_name]
observation = tool(tool_input)
```

Therefore:

```text
LLM
 ↓
Decides which tool is required
 ↓
Generates Tool Call
 ↓
Application receives Tool Call
 ↓
Application executes Tool
 ↓
Tool returns Result
```

---

# 9. How Does the Actual Tool Calling Process Work?

Consider your example:

```text
I have ₹5000.
What is the price of iPhone 17?
And how much money will I have left?
```

## Step 1 — User sends the question

```text
User
 ↓
Application
```

The application sends the question and available tools to the LLM.

---

## Step 2 — LLM decides that a tool is required

The LLM sees:

```text
get_product_price(product)
```

and determines:

```text
I need the price of iPhone 17.
Therefore I need get_product_price().
```

---

## Step 3 — LLM generates a Tool Call

```text
Action: get_product_price("iPhone 17")
```

Important:

> At this point, the function has NOT been executed.

The LLM has only requested the tool.

---

## Step 4 — Application receives the Tool Call

Your application extracts:

```text
Tool Name:
get_product_price

Argument:
iPhone 17
```

---

## Step 5 — Application executes the Tool

Your Python code executes:

```python
get_product_price("iPhone 17")
```

The function returns:

```text
1000
```

---

## Step 6 — Application sends the Tool Result back to the LLM

The application sends:

```text
Observation:
1000
```

to the LLM.

---

## Step 7 — LLM decides what to do next

Now the LLM knows:

```text
iPhone 17 = ₹1000
User has = ₹5000
```

It needs to calculate:

```text
5000 - 1000
```

So it requests another tool:

```text
Action: calculator("5000 - 1000")
```

---

## Step 8 — Application executes the second Tool

```python
calculator("5000 - 1000")
```

Result:

```text
4000
```

---

## Step 9 — LLM gives the Final Answer

The application sends `4000` back to the LLM.

The LLM responds:

```text
The iPhone 17 costs ₹1000.
You will have ₹4000 left.
```

---

# 10. Complete Tool Calling Flow

```text
                    USER
                      |
                      v
                User Question
                      |
                      v
                     LLM
                      |
              Need a Tool?
                 /        \
               No          Yes
               |            |
               v            v
        Final Answer     Tool Call
                            |
                            v
                      Application
                            |
                            v
                      Execute Tool
                            |
                            v
                       Tool Result
                            |
                            v
                           LLM
                            |
                  Need Another Tool?
                      /          \
                    Yes           No
                     |             |
                     v             v
                 Tool Call    Final Answer
```

---

# 11. Tool Calling vs Tool Execution

These are two different things.

## Tool Calling

The LLM requests:

```text
calculator("5000 - 1000")
```

Meaning:

> "I want the calculator tool to perform this operation."

## Tool Execution

The application actually runs:

```python
calculator("5000 - 1000")
```

The tool returns:

```text
4000
```

Therefore:

```text
LLM → Tool Call
Application → Tool Execution
Tool → Tool Result
```

---

# 12. What Is a Tool Result?

A **Tool Result** is the output returned by the tool after the application executes it.

Example:

```text
Tool Call:
get_product_price("iPhone 17")

        ↓

Tool Execution

        ↓

Tool Result:
1000
```

The result is then given back to the LLM.

The LLM can use that result to:

- Answer the user
- Call another tool
- Continue solving the task

---

# 13. Can the LLM Call Multiple Tools?

Yes.

A single user request can require multiple tool calls.

Example:

```text
User:
I have ₹5000.
What is the price of iPhone 17?
How much money will I have left?
```

Flow:

```text
LLM
 ↓
Tool Call #1
get_product_price("iPhone 17")
 ↓
Tool Result
1000
 ↓
LLM
 ↓
Tool Call #2
calculator("5000 - 1000")
 ↓
Tool Result
4000
 ↓
LLM
 ↓
Final Answer
```

---

# 14. Why Do Agents Use a Loop?

Because the LLM may need to call tools multiple times before it can produce the final answer.

Conceptually:

```python
while True:

    response = llm(...)

    if tool_call:
        result = execute_tool(tool_call)

        send_result_back_to_llm(result)

    else:
        return final_answer
```

The loop continues until the LLM decides that no more tools are required.

---

# 15. Your Current Code: Manual Tool Calling

In your code, you created:

```python
tools = {
    "get_product_price": get_product_price,
    "calculator": calculator
}
```

This means:

```text
"get_product_price"
        ↓
get_product_price()

"calculator"
        ↓
calculator()
```

Your LLM is instructed to produce:

```text
Action: get_product_price("iPhone 17")
```

Then you use regex:

```python
match = re.search(
    r"Action:\s*(\w+)\((.*?)\)",
    answer
)
```

You extract:

```python
tool_name = match.group(1)
tool_input = match.group(2)
```

Then you execute:

```python
tool = tools[tool_name]
observation = tool(tool_input)
```

So your current implementation is:

```text
LLM
 ↓
Generates text:
Action: get_product_price("iPhone 17")
 ↓
Regex parses the text
 ↓
Python identifies the tool
 ↓
Python executes the tool
 ↓
Observation
 ↓
LLM
```

This is a **manual / text-based tool-calling implementation**.

---

# 16. Manual Tool Calling vs Native Tool Calling

## Manual Tool Calling

You ask the LLM to produce text:

```text
Action: calculator("5000 - 1000")
```

Then you parse it using regex:

```python
re.search(...)
```

### Problem

The LLM could produce:

```text
calculator(expression="5000 - 1000")
```

or:

```text
I will use calculator("5000 - 1000")
```

or some unexpected format.

Your parser may fail.

---

## Native Tool Calling

Modern LLM APIs can provide a structured tool-call response.

Conceptually:

```json
{
  "name": "calculator",
  "arguments": {
    "expression": "5000 - 1000"
  }
}
```

Now the application does not need to parse natural language with regex.

It can directly get:

```text
Tool:
calculator

Arguments:
expression = "5000 - 1000"
```

and execute the function.

---

# 17. Important: Tool Definitions Are Not the Same as Tool Calls

These are different.

## Tool Definition

Describes what a tool can do.

Example:

```text
calculator(expression)

Description:
Performs mathematical calculations.
```

## Tool Call

The actual request to use that tool.

Example:

```text
calculator("5000 - 1000")
```

So:

```text
Tool Definition
      ↓
Tells the LLM what the tool does

Tool Call
      ↓
Requests execution of that tool
```

---

# 18. Important: The LLM Does Not Automatically Know Your Python Functions

If you have:

```python
def calculator(expression):
    return eval(expression)
```

the LLM does not magically know that this function exists.

You have to expose it to the LLM through:

- Tool definitions
- Tool schemas
- Function descriptions
- Tool-calling API mechanisms

In your current code, you expose the tools through your `system_prompt`:

```text
You have these tools:

get_product_price(product)
calculator(expression)
```

With native tool calling, the tools are usually provided through the API's tool/function schema.

---

# 19. What Determines Whether a Tool Should Be Called?

The LLM considers:

```text
User Intent
      +
Available Tools
      +
Tool Descriptions
      +
Tool Parameters
      ↓
Tool Selection
```

For example:

```text
User:
What is the price of iPhone 17?
```

Matches:

```text
Intent:
Get product price

Tool:
get_product_price(product)
```

Therefore:

```text
Tool Call:
get_product_price("iPhone 17")
```

---

# 20. What Happens If No Tool Can Solve the Request?

If the available tools cannot help, the LLM can answer normally or explain that it cannot perform the requested operation.

Example:

```text
User:
Book me a flight to Delhi.
```

If the application only provides:

```text
calculator()
get_product_price()
```

then there is no flight-booking capability.

The LLM cannot actually book the flight because:

```text
book_flight()
```

was not provided as a tool.

---

# 21. Security Point

The LLM should not have unrestricted access to your application.

Only expose the tools that the LLM is allowed to use.

For example:

```text
Allowed:

get_product_price()
calculator()
search_products()
```

Do not expose dangerous operations unnecessarily.

The application should also validate:

- Tool name
- Arguments
- User permissions
- Authentication
- Authorization
- Input format
- Tool output

The LLM decides **what it wants to do**, but your application should still decide **whether it is actually allowed to do it**.

---

# 22. The Most Important Mental Model

Remember this:

```text
1. User sends request
        ↓
2. LLM sees available tools
        ↓
3. LLM decides whether a tool is required
        ↓
4. LLM generates a Tool Call
        ↓
5. Application receives the Tool Call
        ↓
6. Application validates and executes the Tool
        ↓
7. Tool returns a result
        ↓
8. Application sends the result back to LLM
        ↓
9. LLM decides what to do next
        ↓
10. Another Tool Call OR Final Answer
```

## One-Line Summary

> **LLM decides → LLM generates Tool Call → Application executes → Tool returns Result → Result goes back to LLM → LLM continues or gives Final Answer.**