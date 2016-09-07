# Code written by Kevin Morssink
# Inspired by the IPTV.bundle of Cigaras

APIURL 							= 'https://example.com/jsoniptv/api.php'
HTTP.CacheTime 					= 0
HTTP.Headers['Cache-Control'] 	= 'no-cache'
HTTP.Headers['User-Agent'] 		= 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'

####################################################################################################
def Start():
	ObjectContainer.title1 		= 'JSON IPTV'
	ObjectContainer.art 		= R('ObjectContainerArtBg.jpg')
	DirectoryObject.art 		= R('ObjectContainerArtBg.jpg')
	VideoClipObject.art 		= R('ObjectContainerArtBg.jpg')

####################################################################################################
@handler('/video/jsoniptv', 'JSON IPTV')
def MainMenu():
	global APIURL
	ObjectContainer.title1 = 'Categories'
	DirectoryObject.thumb = R('IconFolder.png')
	
	try:
		categories = JSON.ObjectFromURL(APIURL + '?get_categories')
	except:
		return ObjectContainer(objects = [DirectoryObject(title="Plugin: API is offline or returned invalid JSON")])

	try:
		if categories['error']:
			return ObjectContainer(objects = [DirectoryObject(title="API: " + categories['error'])])
	except:
		if len(categories) == 0:
			return ObjectContainer(objects = [DirectoryObject(title="Plugin: Category list is empty")])
		
		else:
			oc = ObjectContainer()
			for i, category in sorted(categories.iteritems()):
				oc.add(DirectoryObject(
					key = Callback(GetChildrenOfCategory, title=category, categoryId=i),
					title = category
				))	
			
			return oc
		
####################################################################################################
@route('/video/jsoniptv/getchildrenofcategory')
def GetChildrenOfCategory(title, categoryId):
	global APIURL
	title = title[0].upper() + title[1:].lower() # ucfirst
	ObjectContainer.title1 = title + ' channels'
	
	try:
		channels = JSON.ObjectFromURL(APIURL + '?get_channels&category_id=' + categoryId)
	except:
		return ObjectContainer(objects = [DirectoryObject(title="Plugin: API is offline or returned invalid JSON")])
		
	try:
		if channels['error']:
			return ObjectContainer(objects = [DirectoryObject(title="API: " + channels['error'])])
	except:
		if len(channels['channels']) == 0:
			return ObjectContainer(objects = [DirectoryObject(title="Plugin: Channel list is empty")])
		
		else:
			oc = ObjectContainer()
			test = sorted(channels['channels'].items())
			# Why is the content of the channel category Local not sorted and others are?
			#return ObjectContainer(objects = [DirectoryObject(title=str(test))])

			for i, channel in test:
				oc.add(VideoClipObject(
					key 	= Callback(MetadataObject, video_title=channel['channel_title'], video_url=channel['channel_url'], video_summary=channel['channel_summary'], video_thumb=channel['channel_thumbnail'], video_rating=channel['channel_rating']),
					title 	= channel['channel_title'],
					rating 	= float(str(channel['channel_rating'])),
					originally_available_at = Datetime.Now(),
					summary = channel['channel_summary'],
					thumb 	= Resource.ContentsOfURLWithFallback(url=channel['channel_thumbnail'], fallback=R('IconFolder.png')),
					url		= channel['channel_url'],
					items 	= [
						MediaObject(
			                video_codec 			= VideoCodec.H264,
			                audio_codec 			= AudioCodec.AAC,
			                audio_channels 			= 2,
			                protocol                = 'hls',
			                container               = 'mpegts',
			                optimized_for_streaming = True,
			                parts = [
			                    PartObject(
			                        key = Callback(MetadataObject, video_title=channel['channel_title'], video_url=channel['channel_url'], video_summary=channel['channel_summary'], video_thumb=channel['channel_thumbnail'], video_rating=channel['channel_rating'])
			                    )
			                ]
			            )
			        ]
				))
			return oc
		
####################################################################################################
def MetadataObject(video_title, video_url, video_summary, video_thumb, video_rating):
	vco = VideoClipObject(
		key 					= Callback(MetadataObject, video_title=video_title, video_url=video_url, video_summary=video_summary, video_thumb=video_thumb, video_rating=video_rating),			
		title 					= video_title,
		summary 				= video_summary,
		originally_available_at = Datetime.Now(),
		rating 					= float(str(video_rating)),
		url 					= video_url,
		thumb 					= Resource.ContentsOfURLWithFallback(url=video_thumb, fallback=R('IconFolder.png')),
		items = [
            MediaObject(
                video_codec 			= VideoCodec.H264,
                audio_codec 			= AudioCodec.AAC,
                audio_channels 			= 2,
                protocol                = 'hls',
                container               = 'mpegts',
                optimized_for_streaming = True,
                parts = [
                    PartObject(
                        key = HTTP.Request(video_url).content
                    )
                ]
            )
        ]
	)
	return ObjectContainer(objects = [vco])