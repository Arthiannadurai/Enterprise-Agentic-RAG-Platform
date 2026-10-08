import logging
print("its come from logger")
# def get_logger(name: str)->logging.Logger:
#     logging.basicConfig(
#         level=logging.INFO,
#         format=(
#             "%(asctime)s | %(levelname)s | "
#             "%(name)s | %(message)s"
#         )
#     )
#     return logging.getLogger(name)


def get_logger(name: str):
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.setLevel(logging.INFO)

    return logger