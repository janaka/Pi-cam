import flickr

flickr.API_KEY = '72aff1c894a5305e416ab37b3148fd28'
flickr.SECRET = '4670cefe3afd47d9'

getPhotoUrls('sonycameraclub', 'Thumbnail', False)


def getURL(photo, size, equal=False):
    """Retrieves a url for the photo.  (flickr.photos.getSizes)
    
    photo - the photo
    size - what size 'Thumbnail, Small, Medium, Large, Original'
    equal - should width == height?
    """
    method = 'flickr.photos.getSizes'
    data = flickr._doget(method, photo_id=photo.id)
    for psize in data.rsp.sizes.size:
        if psize.label == size:
            if equal and psize.width == psize.height:
                return psize.source
            elif not equal:
                return psize.source
    raise (flickr.FlickrError, "No URL found")

def getPhotoURLs(groupid, size, number, equal=False):
    group = flickr.Group(groupid)
    photos = group.getPhotos(per_page=number)
    urls = []
    for photo in photos:
        try:
            urls.append(getURL(photo, size, equal))
        except flickr.FlickrError:
            if verbose:
                print ("%s has no URL for %s") % (photo, size)
    return urls




