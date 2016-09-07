API documentation
---

You have to build the API yourself and fill it with proper data. But the Plugin will request the following URLs on the location provided in the APIURL variable inside the .bundle file `__init__.py` (on the first line):

To get the category list and fill the first screen
- https://example.com/jsoniptv/api.php?get_categories=1

To get the channels listed inside the selected category
- https://example.com/jsoniptv/api.php?get_channels&category_id=1

To get the proper streaming URL of the selected channel
- https://example.com/jsoniptv/api.php?get_m3u8_url&channel_id=1

Above URLs will report in JSON or plain-text as described below:

In JSON
--

https://example.com/jsoniptv/api.php?get_categories=1

	{"1":"News","2":"Music","3":"Other"}

https://example.com/jsoniptv/api.php?get_channels&category_id=1

	{
	   "channels":{
	      "0":{
	         "id":"1",
	         "channel_title":"CNN",
	         "channel_summary":"The Cable News Network (CNN) is an American basic cable and satellite television channel that is owned by the Turner Broadcasting System division of Time Warner.",
	         "channel_url":"https:\/\/example.com\/jsoniptv\/api.php?get_m3u8_url&channel_id=1",
	         "channel_rating":"10.0",
	         "channel_thumbnail":"https:\/\/example.com/jsoniptv\/image\/1.jpg"
	      }
	   }
	}
	
In Plain Text
--

https://example.com/jsoniptv/api.php?get_m3u8_url&channel_id=1

	https://example.com/playlist/index.m3u8