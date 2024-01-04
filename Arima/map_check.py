import pickle 
import folium

def plot_map(channel, predicted_dredging,channel_1={
    'Area1': (9.955449, 76.266205),
    'Area2': (9.953278, 76.264963),
    'Area3': (9.950183, 76.265216),
    'Area4': (9.947462, 76.266129)
},channel_2= {
    'Area5': (9.954675, 76.261415),
    'Area6': (9.952629, 76.262530),
    'Area7': (9.950613, 76.262305),
    'Area8': (9.950055, 76.261305)
}):
    # print("hhhh",type(channel))
    final_channel = channel_1
    if int(channel) ==2:
    #   print("true")
      final_channel = channel_2

    m = folium.Map(location=[9.953949, 76.263824], zoom_start=15)

    for area, coordinates in final_channel.items():
        color = 'orange'
        if predicted_dredging == 0:
            color = 'red'
        elif predicted_dredging == 1:
            color = 'green'
        folium.Marker(location=coordinates, tooltip=area, icon=folium.Icon(color=color)).add_to(m)

    color = 'orange'
    if predicted_dredging == 0:
        color = 'red'
    elif predicted_dredging == 1:
        color = 'green'
    area_coords = [final_channel[key] for key in final_channel]
    folium.PolyLine(locations=area_coords + [area_coords[0]], color=color).add_to(m)

    legend_html = '''
    <div style="position:fixed; bottom:50px; left:50px; z-index:1000; background:white; padding:5px; border:2px solid grey;">
        <p><span style="color:green;">Low Dredging</span></p>
        <p><span style="color:orange;">Medium Dredging</span></p>
        <p><span style="color:red;">High Dredging</span></p>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    m.save('templates/output.html')
    return m
# plot_map(2,1, {
#     'Area1': (9.968461, 76.242986),
#     'Area2': (9.969007, 76.245615),
#     'Area3': (9.971323, 76.245279),
#     'Area4': (9.970446, 76.241760)
# }
# ,{
#     'Area5': (9.965712, 76.237983),
#     'Area6': (9.967654, 76.240235),
#     'Area7': (9.968383, 76.239697),
#     'Area8': (9.967334, 76.238789)
# })
# with open("plot_map.pkl",'wb') as model_file: 
#     pickle.dump(plot_map,model_file)

plot_map(2, 0)
