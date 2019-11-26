# PDF-dictionary-highlighter
Highlights every word in your PDF given dictionaries.

## Known limitations to be improved in the future
Non-ASCII chars cannot be converted to their English equivalents for comparison because Fitz library which is used for PDF interaction, is incompatible with Python3 and char translation libraries are incompatible with Python2. This means for instance that if your PDF contains the word "Neuchâtel", even if that word is also in one of your dictionaries, it will not be highlighted in the PDF due to the comparison limitations.