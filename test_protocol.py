from mypytest_protocol import support_complex
import numpy as np
c = np.complex64(3+4j)
print(isinstance(c,support_complex))  ## complex64 implements __complex__
## hence compatible

