class Peripheral:
    
    def __init__(self, samplingRate, identifier, lastUpdated, color, icon, text, classification, deviceMac):
        self._samplingRate = samplingRate
        self._identifier = identifier
        self._lastUpdated = lastUpdated
        self._color = color
        self._icon = icon
        self._text = text
        self._classification = classification
        self._deviceMac = deviceMac

    @property
    def samplingRate(self):
        return self._samplingRate
    
    @property
    def identifier(self):
        return self._identifier

    @property
    def lastUpdated(self):
        return self._lastUpdated
    
    @property
    def color(self):
        return self._color

    @property
    def icon(self):
        return self._icon
    
    @property
    def text(self):
        return self._text

    @property
    def classification(self):
        return self._classification

    def getSample(self, consumer):
        return consumer.fetchPeripheralSample(self._deviceMac, self._identifier)