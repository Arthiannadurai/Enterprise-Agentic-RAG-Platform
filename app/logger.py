import logging
# def get_logger(name: str) -> logging.Logger:
print("its come from logger")
def get_logger(name: str)->logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        )
    )
    return logging.getLogger(name)