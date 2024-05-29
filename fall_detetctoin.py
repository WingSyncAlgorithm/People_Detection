from utils import FeatureExtractor, KeyPoints



if __name__ == "__main__":

    featureextractor = FeatureExtractor()
    cost = featureextractor.realTimeVideo("c.mp4", "Division", False)
