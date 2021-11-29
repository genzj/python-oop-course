class IndexHandler:
    singleton = None

    @classmethod
    def get_singleton(cls):
        if cls.singleton is None:
            cls.singleton = IndexHandler()
        return cls.singleton

    @staticmethod
    def get_instance():
        return IndexHandler()
