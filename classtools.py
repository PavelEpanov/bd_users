class AttrDisplay:
    # Предоставляет наследуемый метод перегрузки отображения, который показывает
    # экземпляры с их именами классов и пары имя=значение для каждого атрибута,
    # сохраненного в самом экземпляре (но не атрибутов, унаследованных от его классов) .
    # Может соединяться с любым классом и будет работать на любом экземпляре.

    def _gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f"{key}={getattr(self, key)}")
            #attrs.append('% s = % s' % (key, getattr(self, key)))
        return ",".join(attrs)

    def __repr__(self):
        return f"[{self.__class__.__name__}:{self._gatherAttrs()}]"
        #return '[ %s: %s]' % (self.__class__.__ name__, self.gatherAttrs())


if __name__ == "__main__":
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
    class SubTEst(TopTest):
        pass

    X, Y = TopTest(), SubTEst() # Создать 2 экземпляра
    print(X) # Показать все атрибуты экземпляров
    print(Y)
