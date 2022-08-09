schema = "{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"version\": \"1.0.0\",\n    \"title\": \"Event\"\n  },\n  \"paths\": {},\n  \"components\": {\n    \"schemas\": {\n      \"Event\": {\n        \"type\": \"object\",\n        \"required\": [\n          \"key1\",\n          \"key2\",\n          \"key3\",\n          \"key4\"\n        ],\n        \"properties\": {\n          \"key1\": {\n            \"type\": \"string\"\n          },\n          \"key2\": {\n            \"type\": \"string\"\n          },\n          \"key3\": {\n            \"type\": \"string\"\n          },\n          \"key4\": {\n            \"type\": \"string\"\n          }\n        }\n      }\n    },\n    \"examples\": {\n      \"My-Test-Event\": {\n        \"value\": {\n          \"key1\": \"lol\",\n          \"key2\": \"hi\",\n          \"key3\": \"there\",\n          \"key4\": \"hi to you too\"\n        }\n      }\n    }\n  }\n}"
