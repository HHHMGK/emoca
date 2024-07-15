import sys
from trace import Trace

# Khởi tạo một đối tượng Tracer với các tùy chọn mong muốn
tracer = Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    countfuncs = False,
    count=0,
    timing = True
)

# Chạy mã của bạn dưới dạng một module hoặc script
tracer.run('import gdl_apps.EMOCA.demos.test_emoca_on_images')

# Lấy danh sách các file đã được chạy
result = tracer.results()
result.write_results(show_missing=0,coverdir='gdl_apps/EMOCA/demos/trace_vizier')