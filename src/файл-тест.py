#!/usr/bin/env python3

# Это тест большого файла с Unicode символами
# This is a large file test with Unicode characters

import random
import string

# Generate large content with Unicode
unicode_chars = 'файлданныетест测试数据' + string.ascii_letters + string.digits

# Create large content
large_content = ''.join(random.choice(unicode_chars) for _ in range(1000000))

print('Large Unicode file generated successfully!')
print(f'Content length: {len(large_content)} characters')