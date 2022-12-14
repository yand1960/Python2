import logging

logger = logging.getLogger("MyLogger")
# logger.addHandler(logging.StreamHandler())
handler = logging.FileHandler("data/log.txt", encoding="utf-8")
handler.setFormatter(logging.Formatter( fmt='%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    logger.debug("It is debug")
    logger.info("It is info")
    logger.warning("It is warning")
    logger.error("It is error")
    logger.critical("It is critical")