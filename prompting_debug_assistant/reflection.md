# Reflection on AI-Assisted Debugging

## Introduction
During this project, I created 5 buggy code snippets. I then used AI to find and correct bugs in each file. After AI gave me the corrected form of each file and explanations for bugs, I manually tested the new codes and verified that the bugs were resolved. 

## AI Strengths
AI performed well in the ares of finding the exact bug and its line, and suggesting what should exactly change in the code to fix it. For example, syntax errors and common mistakes involving conditional statements or built-in methods were relatively straightforward for it to identify. It also explained the root causes of errors, which made it easier to understand why the original code was not behaving as expected. Another strength was its speed. Instead of manually searching through documentation or spending considerable time identifying an error, I could provide the code and receive a potential explanation and solution within seconds. It was also pretty quick to create and present the written information in a required markdown structure, which increased my productivity.  

## AI Weaknesses
Despite its strengths, AI was not always reliable. In one case, I did not provide sufficient context about the original bug before asking it to review the corrected code. It made an assumption about what the original problem had been, but that assumption was incorrect. The actual issue I had addressed in that file was completely different. This demonstrated that AI does not necessarily understand the original intention behind a piece of code. When context is missing, it may confidently provide an explanation that sounds reasonable but does not reflect the actual situation.

## Human Role
Human involvement was essential throughout the debugging process. I had to understand the original requirements, evaluate whether the AI-generated changes addressed the actual problems, and decide whether additional modifications were necessary. After applying code that AI suggested, it's important that humans manually run and test it to make sure that the bug is really fixed and the existing application functionality is intact. 

## Conclusion
Overall, AI made the debugging process faster and more efficient, particularly when dealing with common programming errors. However, I would not completely trust its suggestions without verification. During this process, we have to make sure to critically check and verify AI suggestions before committing the code. My experience showed that AI is most useful as an assistant rather than an independent decision-maker.

One of my key takeaways is that providing sufficient context in prompts significantly affects the quality of AI-generated responses; otherwise, AI might invent the context that doesn't reflect reality. In real-world software development, AI can reduce the time spent on repetitive debugging tasks, but critical thinking is still essential to ensure that solutions are correct, reliable, and maintainable.
