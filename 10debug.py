import logging

# logging.basicConfig(
#     level=logging.DEBUG,  # 日志级别
#     format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
#     datefmt="%Y-%m-%d %H:%M:%S",  # 时间格式
#     filename="error.log",  # 日志文件名
#     filemode="w"  # 写入模式，覆盖文件内容
# )

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")



# 自定义日志记录器
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器
file_handler = logging.FileHandler('app-error.log')
file_handler.setLevel(logging.DEBUG)

# 创建一个控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# 创建一个格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
