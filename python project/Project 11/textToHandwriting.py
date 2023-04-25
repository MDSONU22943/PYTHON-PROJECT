import pywhatkit as pw

txt="""Python is a high-level, interpreted programming language that was first released in 1991. It is widely used for web development, data analysis, artificial intelligence, machine learning, scientific computing, and many other applications.
Python is known for its simple and elegant syntax, which makes it easy to read and write code. It also has a large standard library that provides access to a wide range of functions and modules, making it a very versatile language. Python's popularity is due in part to its ease of use and the availability of a wide range of libraries and frameworks, such as Django and Flask for web development, NumPy and Pandas for data analysis, and TensorFlow and PyTorch for machine learning.
Python is an interpreted language, which means that it doesn't need to be compiled before it can be run. Instead, the code is interpreted on the fly, which makes development faster and easier. Python is also a cross-platform language, which means that it can run on different operating systems, such as Windows, macOS, and Linux."""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print("END")