import os, re, json
indexFilename = "index.json"

regex = re.compile("^(?!(?:\._|\.).*).*\.json$")

platformWallpaperPacks = [f for f in os.listdir('.') if os.path.isdir(f)]
platformWallpaperPacks.sort()

index = {
    "baseUri": "https://raw.githubusercontent.com/magneticchen/Daijishou/main/themes/platform_wallpaper_packs/",
    "platformWallpaperPackList": []
}


for d in platformWallpaperPacks:
    print(d)
    platformWallpaperPackDir = d
    files = [f for f in os.listdir(platformWallpaperPackDir) if os.path.isfile(platformWallpaperPackDir+'/'+f)]
    # files.sort()

    for f in files:
        if f == indexFilename:
            f = platformWallpaperPackDir+'/'+f
            with open(f) as jsonFile:
                platformWallpaperPackIndex = json.load(jsonFile)
                platformWallpaperPackName = platformWallpaperPackIndex['name']
                platformWallpaperPackDescription = platformWallpaperPackIndex['description']
                platformWallpaperPackAuthors = platformWallpaperPackIndex['authors']
                platformWallpaperPackPreviewThumbnailFilename = platformWallpaperPackIndex['previewThumbnailFilename']
                index['platformWallpaperPackList'].append({
                    "platformWallpaperPackRootPath": platformWallpaperPackDir,
                    # "platformWallpaperPackIndexPath": f,
                    "platformWallpaperPackPreviewThumbnailPath": platformWallpaperPackDir+'/'+platformWallpaperPackPreviewThumbnailFilename,
                    "platformWallpaperPackAuthors": platformWallpaperPackAuthors,
                    "platformWallpaperPackName": platformWallpaperPackName,
                    "platformWallpaperPackDescription": platformWallpaperPackDescription
                })

with open(indexFilename, 'w') as outfile:
    json.dump(index, outfile, indent=2, sort_keys=True)