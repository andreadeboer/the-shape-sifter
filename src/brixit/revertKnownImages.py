import commonUtils as cu
import os


def RevertUnknownFiles():
    """ Moves files from the unknow folder back to the known folder and erases knownparts.txt"""
    walker = os.walk(cu.settings.labelledPartsPath, topdown=False)
    for root, dirs, files in walker:
        for file in files:
            srcPath = os.path.join(root, file)
            dstPath = os.path.join(cu.settings.unlabelledPartsPath, file)
            try:
                os.replace(srcPath, dstPath)
            except Exception as e:
                continue

    if os.path.exists(cu.settings.labelledPartsTxt):
        os.remove(cu.settings.labelledPartsTxt)


if __name__ == "__main__":
    RevertUnknownFiles()
