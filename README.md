# json_base64_decoder

## A simple and basic Base64 decoder for JSON.

### Key points:
- Reads JSON file input
- decodes Base64 encoded VALUES only
- prints sorted keys with decoded values

## Installation:
```bash
pip3 install -r requirements.txt
```

## Usage:
```bash
python3 json_b64_decoder -i /path/to/file -k specific_key
```

## Arguments:
```
-i    json file to decode           [REQUIRED]
-k    specific json key to decode   [OPTIONAL]
```
