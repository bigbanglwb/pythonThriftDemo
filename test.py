import sys
import time
import logging
import time
from jaeger_client import Config
def init_tracer(service):
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            # 'local_agent': {
            #     'reporting_host': '127.0.0.1',
            #     'reporting_port': '14268',
            # },
            'logging': True,
        },  
        service_name=service,
        validate=True,
    )
    # this call also sets opentracing.tracer
    return config.initialize_tracer()

def say_hello(hello_to):
    with tracer.start_span('say-hello') as span:
        # 标签 tag，元数据
        span.set_tag('hello-to', hello_to)

        # 日志 log，包含时间戳和一些数据
        hello_str = 'Hello, %s!' % hello_to
        span.log_kv({'event': 'string-format', 'value': hello_str})

        print(hello_str)
        span.log_kv({'event': 'println'})

assert len(sys.argv) == 2

# 初始化全局 trace
# 将 tracer 开始的所有 span 标记为源自 hello-world 服务
tracer = init_tracer('hello-world')

hello_to = sys.argv[1]
say_hello(hello_to)

# span 有内部缓冲区，由后台线程刷新
# yield to IOLoop to flush the spans
time.sleep(2)
tracer.close()