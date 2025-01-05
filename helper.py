import re
from typing import Any, Dict, List, Union
from pydantic import BaseModel

class CodeBlock(BaseModel):
    """A class that represents a code block."""

    """The code to execute."""
    code: str

    """The language of the code."""
    language: str

CODE_BLOCK_PATTERN = r"```[ \t]*(\w+)?[ \t]*\r?\n(.*?)\r?\n[ \t]*```" # pattern to extract code blocks from a message

class MarkdownCodeExtractor:
    """A class that extracts code blocks from a message using Markdown syntax."""
    
    def content_str(self,content: Union[str, List[Dict[str, Any]], None]) -> str:
        """Converts `content` into a string format.
        This function processes content that may be a string, a list of dictionary of string or None,
        and converts it into a string. Text is directly appended to the result string.
        If the content is None, an empty string is returned.
        
        Args:
        - content (Union[str, List, None]): The content to be processed. Can be a string, a list of dictionaries
        representing text or None.
        
        Returns:
        str: A string representation of the input content.
    """
        
        if content is None:
            return "" # return empty string if no content
        
        if isinstance(content, str):
            return content # return content if it is a string
        
        if not isinstance(content, list):
            raise TypeError(f"content must be None, str, or list, but got {type(content)}")
        
        rst = "" # string representing the content

        for item in content:
            if not isinstance(item, dict):
                raise TypeError("Wrong content format: every element should be dict if the content is a list.")
            assert "content" in item, "Wrong content format. Missing 'content' key in content's dict."
            rst += item["content"] # append the content to the result string
        return rst
        
    def infer_lang(self,code: str) -> str:
        """infer the language for the code.
        """
        if code.startswith("python ") or code.startswith("pip") or code.startswith("python3 "):
            return "sh"
        # check if code is a valid python code
        try:
            compile(code, "test", "exec")
            return "python"
        except SyntaxError:
            # not a valid python code
            return "unknown"

    def extract_code_blocks(self, message: Union[str, List[Dict[str, Any]], None]) -> List[CodeBlock]:
        """Extract code blocks from a message. If no code blocks are found,
        return an empty list.

        Args:
            message (str): The message to extract code blocks from.

        Returns:
            List[CodeBlock]: The extracted code blocks or an empty list.
        """

        text = self.content_str(message) # convert the message to a string

        match = re.findall(CODE_BLOCK_PATTERN, text, flags=re.DOTALL) # find all code blocks in the message
        if not match:
            return [] # return empty list if no code blocks are found
        
        code_blocks = []
        for lang, code in match:
            if lang == "":
                lang = self.infer_lang(code) # infer the language of the code
            if lang == "unknown":
                lang = ""
            code_blocks.append(CodeBlock(code=code, language=lang)) # append the code block to the list of code blocks
        return code_blocks
    
