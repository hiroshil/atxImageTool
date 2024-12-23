import json
import atlas_pb2

json_data = '''
{"Canvas":{"Width":1920,"Height":1080},"Block":[{"filename":"bg010d","filenameOld":"bg010d","blend":"norm","id":0,"anchorX":0.0,"anchorY":0.0,"width":1920.0,"height":1080.0,"offsetX":0.0,"offsetY":0.0,"priority":0,"Mesh":[{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":0.0,"srcOffsetY":0.0,"texU1":0.00146484375,"texV1":0.00146484375,"texU2":0.12353515625,"texV2":0.12353515625,"viewX":3.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":250.0,"srcOffsetY":0.0,"texU1":0.12646484375,"texV1":0.00146484375,"texU2":0.24853515625,"texV2":0.12353515625,"viewX":259.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":500.0,"srcOffsetY":0.0,"texU1":0.25146484375,"texV1":0.00146484375,"texU2":0.37353515625,"texV2":0.12353515625,"viewX":515.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":750.0,"srcOffsetY":0.0,"texU1":0.37646484375,"texV1":0.00146484375,"texU2":0.49853515625,"texV2":0.12353515625,"viewX":771.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1000.0,"srcOffsetY":0.0,"texU1":0.50146484375,"texV1":0.00146484375,"texU2":0.62353515625,"texV2":0.12353515625,"viewX":1027.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1250.0,"srcOffsetY":0.0,"texU1":0.62646484375,"texV1":0.00146484375,"texU2":0.74853515625,"texV2":0.12353515625,"viewX":1283.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1500.0,"srcOffsetY":0.0,"texU1":0.75146484375,"texV1":0.00146484375,"texU2":0.87353515625,"texV2":0.12353515625,"viewX":1539.0,"viewY":3.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":85.0,"offsetY":125.0,"srcOffsetX":1750.0,"srcOffsetY":0.0,"texU1":0.87646484375,"texV1":0.00146484375,"texU2":0.95947265625,"texV2":0.12353515625,"viewX":1795.0,"viewY":3.0,"width":170.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":0.0,"srcOffsetY":250.0,"texU1":0.00146484375,"texV1":0.12646484375,"texU2":0.12353515625,"texV2":0.24853515625,"viewX":3.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":250.0,"srcOffsetY":250.0,"texU1":0.12646484375,"texV1":0.12646484375,"texU2":0.24853515625,"texV2":0.24853515625,"viewX":259.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":500.0,"srcOffsetY":250.0,"texU1":0.25146484375,"texV1":0.12646484375,"texU2":0.37353515625,"texV2":0.24853515625,"viewX":515.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":750.0,"srcOffsetY":250.0,"texU1":0.37646484375,"texV1":0.12646484375,"texU2":0.49853515625,"texV2":0.24853515625,"viewX":771.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1000.0,"srcOffsetY":250.0,"texU1":0.50146484375,"texV1":0.12646484375,"texU2":0.62353515625,"texV2":0.24853515625,"viewX":1027.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1250.0,"srcOffsetY":250.0,"texU1":0.62646484375,"texV1":0.12646484375,"texU2":0.74853515625,"texV2":0.24853515625,"viewX":1283.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1500.0,"srcOffsetY":250.0,"texU1":0.75146484375,"texV1":0.12646484375,"texU2":0.87353515625,"texV2":0.24853515625,"viewX":1539.0,"viewY":259.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":85.0,"offsetY":125.0,"srcOffsetX":1750.0,"srcOffsetY":250.0,"texU1":0.87646484375,"texV1":0.12646484375,"texU2":0.95947265625,"texV2":0.24853515625,"viewX":1795.0,"viewY":259.0,"width":170.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":0.0,"srcOffsetY":500.0,"texU1":0.00146484375,"texV1":0.25146484375,"texU2":0.12353515625,"texV2":0.37353515625,"viewX":3.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":250.0,"srcOffsetY":500.0,"texU1":0.12646484375,"texV1":0.25146484375,"texU2":0.24853515625,"texV2":0.37353515625,"viewX":259.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":500.0,"srcOffsetY":500.0,"texU1":0.25146484375,"texV1":0.25146484375,"texU2":0.37353515625,"texV2":0.37353515625,"viewX":515.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":750.0,"srcOffsetY":500.0,"texU1":0.37646484375,"texV1":0.25146484375,"texU2":0.49853515625,"texV2":0.37353515625,"viewX":771.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1000.0,"srcOffsetY":500.0,"texU1":0.50146484375,"texV1":0.25146484375,"texU2":0.62353515625,"texV2":0.37353515625,"viewX":1027.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1250.0,"srcOffsetY":500.0,"texU1":0.62646484375,"texV1":0.25146484375,"texU2":0.74853515625,"texV2":0.37353515625,"viewX":1283.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1500.0,"srcOffsetY":500.0,"texU1":0.75146484375,"texV1":0.25146484375,"texU2":0.87353515625,"texV2":0.37353515625,"viewX":1539.0,"viewY":515.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":85.0,"offsetY":125.0,"srcOffsetX":1750.0,"srcOffsetY":500.0,"texU1":0.87646484375,"texV1":0.25146484375,"texU2":0.95947265625,"texV2":0.37353515625,"viewX":1795.0,"viewY":515.0,"width":170.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":0.0,"srcOffsetY":750.0,"texU1":0.00146484375,"texV1":0.37646484375,"texU2":0.12353515625,"texV2":0.49853515625,"viewX":3.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":250.0,"srcOffsetY":750.0,"texU1":0.12646484375,"texV1":0.37646484375,"texU2":0.24853515625,"texV2":0.49853515625,"viewX":259.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":500.0,"srcOffsetY":750.0,"texU1":0.25146484375,"texV1":0.37646484375,"texU2":0.37353515625,"texV2":0.49853515625,"viewX":515.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":750.0,"srcOffsetY":750.0,"texU1":0.37646484375,"texV1":0.37646484375,"texU2":0.49853515625,"texV2":0.49853515625,"viewX":771.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1000.0,"srcOffsetY":750.0,"texU1":0.50146484375,"texV1":0.37646484375,"texU2":0.62353515625,"texV2":0.49853515625,"viewX":1027.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1250.0,"srcOffsetY":750.0,"texU1":0.62646484375,"texV1":0.37646484375,"texU2":0.74853515625,"texV2":0.49853515625,"viewX":1283.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":125.0,"srcOffsetX":1500.0,"srcOffsetY":750.0,"texU1":0.75146484375,"texV1":0.37646484375,"texU2":0.87353515625,"texV2":0.49853515625,"viewX":1539.0,"viewY":771.0,"width":250.0,"height":250.0},{"texNo":0,"offsetX":85.0,"offsetY":125.0,"srcOffsetX":1750.0,"srcOffsetY":750.0,"texU1":0.87646484375,"texV1":0.37646484375,"texU2":0.95947265625,"texV2":0.49853515625,"viewX":1795.0,"viewY":771.0,"width":170.0,"height":250.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":0.0,"srcOffsetY":1000.0,"texU1":0.00146484375,"texV1":0.50146484375,"texU2":0.12353515625,"texV2":0.54052734375,"viewX":3.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":250.0,"srcOffsetY":1000.0,"texU1":0.12646484375,"texV1":0.50146484375,"texU2":0.24853515625,"texV2":0.54052734375,"viewX":259.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":500.0,"srcOffsetY":1000.0,"texU1":0.25146484375,"texV1":0.50146484375,"texU2":0.37353515625,"texV2":0.54052734375,"viewX":515.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":750.0,"srcOffsetY":1000.0,"texU1":0.37646484375,"texV1":0.50146484375,"texU2":0.49853515625,"texV2":0.54052734375,"viewX":771.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":1000.0,"srcOffsetY":1000.0,"texU1":0.50146484375,"texV1":0.50146484375,"texU2":0.62353515625,"texV2":0.54052734375,"viewX":1027.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":1250.0,"srcOffsetY":1000.0,"texU1":0.62646484375,"texV1":0.50146484375,"texU2":0.74853515625,"texV2":0.54052734375,"viewX":1283.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":125.0,"offsetY":40.0,"srcOffsetX":1500.0,"srcOffsetY":1000.0,"texU1":0.75146484375,"texV1":0.50146484375,"texU2":0.87353515625,"texV2":0.54052734375,"viewX":1539.0,"viewY":1027.0,"width":250.0,"height":80.0},{"texNo":0,"offsetX":85.0,"offsetY":40.0,"srcOffsetX":1750.0,"srcOffsetY":1000.0,"texU1":0.87646484375,"texV1":0.50146484375,"texU2":0.95947265625,"texV2":0.54052734375,"viewX":1795.0,"viewY":1027.0,"width":170.0,"height":80.0}],"Attribute":[{"id":-1,"x":0,"y":0,"width":0,"height":0,"color":0}]}]}
'''

#data = json.loads(json_data)

with open('test/atlas.json', 'r') as file:
    data = json.load(file)

atlas_message = atlas_pb2.Atlas()

atlas_message.Canvas.Width = data['Canvas']['Width']
atlas_message.Canvas.Height = data['Canvas']['Height']

for block_data in data['Block']:
    block_message = atlas_message.Block.add()
    block_message.filename = block_data['filename']
    block_message.filenameOld = block_data['filenameOld']
    #block_message.blend = block_data['blend']
    block_message.id = block_data['id']
    block_message.anchorX = block_data['anchorX']
    block_message.anchorY = block_data['anchorY']
    block_message.width = block_data['width']
    block_message.height = block_data['height']
    block_message.offsetX = block_data['offsetX']
    block_message.offsetY = block_data['offsetY']
    block_message.priority = block_data['priority']

    for mesh_data in block_data['Mesh']:
        mesh_message = block_message.Mesh.add()
        mesh_message.texNo = mesh_data['texNo']
        mesh_message.offsetX = mesh_data['offsetX']
        mesh_message.offsetY = mesh_data['offsetY']
        mesh_message.srcOffsetX = mesh_data['srcOffsetX']
        mesh_message.srcOffsetY = mesh_data['srcOffsetY']
        mesh_message.texU1 = mesh_data['texU1']
        mesh_message.texV1 = mesh_data['texV1']
        mesh_message.texU2 = mesh_data['texU2']
        mesh_message.texV2 = mesh_data['texV2']
        mesh_message.viewX = mesh_data['viewX']
        mesh_message.viewY = mesh_data['viewY']
        mesh_message.width = mesh_data['width']
        mesh_message.height = mesh_data['height']

    for attribute_data in block_data['Attribute']:
        attribute_message = block_message.Attribute.add()
        attribute_message.id = attribute_data['id']
        attribute_message.x = attribute_data['x']
        attribute_message.y = attribute_data['y']
        attribute_message.width = attribute_data['width']
        attribute_message.height = attribute_data['height']
        attribute_message.color = attribute_data['color']

with open('atlas.pb', 'wb') as f:
    #print(atlas_message.SerializeToString() + b'\x6A\x04\x6E\x6F\x72\x6D')
    f.write(atlas_message.SerializeToString() + b'\x6A\x04\x6E\x6F\x72\x6D')
