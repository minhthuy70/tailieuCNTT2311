# Automated Monitoring and Control System for Shrimp Farms

> Chuy?n ??i t? `2015 Automated monitoring and control system for shrimp farms based on embedded system and wireless sensor network.pdf`. N?i dung ???c gi? theo t?ng trang ?? ??i chi?u v?i PDF g?c.

- **S? trang:** 5
- **Ngu?n:** `Thamkhao/2015 Automated monitoring and control system for shrimp farms based on embedded system and wireless sensor network.pdf`

## Trang 1

Automated Monitoring and Control System for 
Shrimp Farms Based on Embedded System and 
Wireless Sensor Network 
Nguyen Tang Kha Duyl, Nguyen Dinh Tu2, Tra Hoang Son3, and Luong Hong Duy Khanh4 
1,2,3Department of Electronics and Telecommunication Engineering, Can Tho University, Vietnam 
4Department of Automation Technology, Can Tho University, Vietnam 
E-mails:ntkduy@ctu.edu.vnl.{tulOl0742;sonl010433;khanhll109S4}@student.ctu.edu.vn 
Abstract-This paper presents a versatile solution in an effort 
of improving the accuracy in monitoring the environmental 
conditions and reducing manpower for industrial households 
shrimp farming. A ZigBee-based wireless sensor network (WSN) 
was used to monitor the critical environmental conditions and all 
the control processes are done with the help of a series of low­
power 
embedded 
MSP430 
microcontrollers 
from 
Texas 
Instruments. This system is capable of collecting, analyzing and 
presenting 
data 
on 
a 
Graphical 
User 
Interface 
(GUI), 
programmed with LabVIEW. It also allows the user to get the 
updated sensor information online based on Google Spreadsheets 
application, via Internet connectivity, or at any time through the 
SMS gateway service and sends alert message promptly enabling 
user interventions when needed. Thereby the system minimizes 
the effects of environmental fluctuations caused by sudden 
changes and reduces the expended labor power of farms. Because 
of that, the proposed system saves the cost of hiring labor as well 
as the electricity usage. The design promotes a versatile, low-cost, 
and commercial version which will function best for small to 
medium sized farming operations as it does not require any 
refitting or reconstruction of the pond. 
Keywords-Aquaculture, 
CC2530, MSP430, 
Wireless Sensor 
Networks (WSN), ZigBee. 
I. 
INTRODUCTION 
In recent years, the development of shrimp farming has 
been rapidly improving in the Mekong Delta in south-east 
Vietnam. Successful shrimp farming is reliant on management 
of the environment as well as good fundamentals such as good 
seeds 
and 
quality 
food. 
Currently, 
famers 
monitor 
the 
environmental 
conditions 
in 
the 
pond 
manually 
and 
irregularly, mostly according to the farmers' experience which 
is time-consuming and costly in terms of manpower. The 
monitoring is usually only done when 
the farmer 
has 
discovered the abnormal condition of the shrimp or when 
environmental 
factors 
change 
dramatically. 
When 
the 
phenomenon occurs, the procedure to help rebalance the 
farming environment is usually very complex and expensive. 
This 
causes 
environmental 
factors 
to 
be 
monitored 
ineffectively. 
Commonly, shrimp farmers use mechanical paddle-wheels 
that have to be turned on and off manually to slap, beat and 
chum oxygen into the surface of the water. The system is 
operated manually based on experience and not based on any 
actual measurement mechanism. The operation of the device 
978-1-4799-6085-9/15/$31.00 ©2015 IEEE 
by 
hand 
causes 
huge 
waste 
of 
power. 
Therefore, 
the 
monitoring of the environment on a regular basis and a 
mechanism for automated control automation is essential. 
Currently, 
a 
number 
of 
shrimp 
farms 
closed 
and 
automation is being applied in the industry. However, these 
models require a huge initial investment cost (minimum of 
three hundred thousand USD to one hectare) and are only 
suitable for large-scale farming businesses [9]. These models 
are beyond the investment capacity of shrimp farms of small 
and medium scale because rehabilitation and reconstruction of 
the entire pond system is required. Soonhee Han et al. has 
designed and built an environmental monitoring system for 
aquaculture farms [2], and sends alerts when environmental 
factors can no longer be guaranteed. However, this system is 
based on a wired network, so the transmission is not only 
problematic, but it is also difficult to expand. 
By examining the actual needs of enterprises of small and 
medium sizes, we found that automating some tasks in a 
scientific way allows us to not only solve the problem of 
ineffective 
human 
resources 
but 
also 
minimize 
power 
consumption. At the same time, research also indicates that 
factors like stratified water temperature, pH, and dissolved 
oxygen (DO) levels in the water are particularly important. 
Based on the information gathered, we propose a low-cost 
system, that is highly interactive and easy-to-use to monitor 
the possible weak operating environment and some automated 
workflows. The system provides two important features as 
follows: 
• 
Continuous monitoring: Our system monitors and 
records water quality around the clock, based on a 
Wireless Sensor Network, providing continuous data 
that can be used to identify trends and improve 
production. Almost any sensor can be used but 
currently our system monitors three critical parameters 
including dissolved oxygen, temperature, and pH. 
Sensors can measure data at any interval depending on 
the determinations of the farm operators. Through the 
use 
of 
mathematical 
algorithms, 
supported 
by 
LabVIEW, operators can store processed data in the 
units of their choice, simplifying data analysis. 
• 
Automated Control: Aerators, pumps, alarms, or other 
electrical devices can be controlled based on measured 
conditions, 
time 
schedule, 
or user 
requests. 
For

> H?nh ?nh/s? ?? trong trang: 1. N?i dung h?nh ???c gi? trong PDF g?c; ch? th?ch ??c ???c ?? n?m trong ph?n v?n b?n tr?n.

## Trang 2

example, aerators can be turned on (day or night) 
when 
DO 
measurements 
reach 
a 
preset 
value. 
Together 
with 
continuous 
monitoring, 
automated 
control keeps the system operating efficiently and 
evenly. 
The remainder of the report 
presents 
the 
following 
sections. Section II will describe the requirements for system 
design. Section III introduces the system architecture based on 
design 
requirements. 
The 
system 
development 
will 
be 
discussed in detail in section IV. In section V, some initial 
results obtained will be presented. Section VI concludes and 
suggests subsequent development of the subject. 
II. 
SYSTEM REQUIREMENTS 
For effective management of shrimp ponds, we need early 
detection of disease problems and the capacity to implement 
appropriate 
responses 
before 
an 
outbreak 
becomes 
uncontrollable [10]. In most ponds, changes in the health of 
the shrimp only become apparent over time based on a 
combination of observations on the condition of shrimp, 
consumption of food quantity, 
water quality, 
etc. More 
importantly any changes of the environmental factors in the 
pond will contribute significantly to the overall decline in the 
total health of the shrimp overall. It is also noted that 
environmental factors in the ponds are heterogeneous and 
constantly changing in many ways based on each region, 
weather, growing conditions, etc. This further complicates 
shrimp farming. Hence, the importance of monitoring these 
conditions correctly in terms of continuity using monitoring 
points of sufficient quantity to arrive at accurate representative 
monitoring is essential. A wireless sensor network is an 
advanced solution compared to traditional monitoring. Sensor 
nodes can be deployed inside the pond which is also an 
economical savings, and at the same time a way to implement 
monitoring, control and long-term research. 
The proposed monitoring and control system should meet 
the following requirements: 
1) Systematic 
• 
Work to be done at the same place, same time each 
day or each month. 
• 
Work 
to 
be 
performed 
and repeated 
at 
regular 
intervals. 
2) Responsive 
• 
The information must be available when required. 
• 
Information must be presented in an understandable 
user friendly way. 
3) Interactive 
• 
Allows user response based on the data collected to 
analyze prospective problems. 
• 
Provides the ability to react promptly to the problems 
encountered. 
4) Predictive 
• 
Data can be used for planning and decision making in 
the future. 
o 
Sensors (End devices) 
V 
Actuators (End devices) 
o 
Cluster head (Router) 
Management (Coordinator) 
v 
000 
000 
1::,. Pond 1 
000 
1::,. 
Pond 2 
LabVIEW 
MSP430 
 
- 
... 
Fig. 1. System architecture of the proposed design. 
III. 
SYSTEM ARCHITECTURE 
Figure 1 shows the most important modules that make up 
our proposed system. To meet the requirements in the 
previous section, the system will be developed based on the 
architecture suggested by A. Mainwaring [1] which has been 
discussed in [4] and [5]. 
To support the scalability of the system, we used three 
models of sensor nodes. First, we built a wireless sensor 
network to collect information in each separate pond, the 
network consists of multiple nodes, and each node will be 
used to obtain the critical sensor information. Next, the 
wireless control network is used to control the oxygen 
pumping system at each pond. Then, the sensor nodes as well 
as control nodes in each pond wirelessly communicate with 
the master station through a node called the cluster header. 
Finally, a management station which is the heart of the 
proposed system is built and is responsible for many tasks 
including gathering sensor information, controlling oxygen 
pumps, etc. All wireless protocols used to communicate 
between nodes in the sensor network systems are based on the 
IEEE 802.11.4 standard which was selected for the design 
because it requires low power consumption. 
Principle of Operation: 
The data gathered from the sensor nodes is sent to the 
cluster head, and the cluster head is responsible for data 
transmission to the base station. The data is then analyzed and 
presented on a graphical user interface, programmed by 
LabVIEW. The data is sent to the base station in a time frame 
consistent with each selected measurement parameter based on 
material in [10]. This time frame can be appropriately changed 
according to the analysis on gathered environmental factors.

> H?nh ?nh/s? ?? trong trang: 4. N?i dung h?nh ???c gi? trong PDF g?c; ch? th?ch ??c ???c ?? n?m trong ph?n v?n b?n tr?n.

## Trang 3

• Zig Bee Coordinator (FFD) 
• Zig Bee Router (FFD) 
• Zig Bee End Device (RFD or FFD) 
- Mesh Link 
Fig. 2. Mesh topology for the proposed monitoring and control system 
The system also provides two options for the purpose of 
increasing the user's interaction with the system. The fIrst 
option allows the user to retrieve up-to-date information about 
the environmental factors in the pond and control equipment 
easily through the SMS gateway. It provides great utility for 
the user as they can access the information or receive 
warnings (when the elements in the pond change and exceed 
certain level) at any location where GSM services exist. 
The other option allows the user to access information 
about 
environmental 
factors 
in 
pond 
via 
a 
web-based 
application 
called 
Google Spreadsheets. 
The 
application 
enables the user to observe the data anywhere that they can 
connect to the Internet. 
IV. 
SYSTEM DEVELOPMENTS 
In 
accordance 
with 
the 
overall 
system 
architecture 
analysis, the implementation of the system consisted of 
protocol, hardware, and software development. 
A. 
Routing Protocol Design 
In 
order 
to 
make 
in-network 
communications 
more 
effIcient, we used the MESH topology with node types 
defIned as follows: (1) end devices (for sensor nodes and 
control nodes); (2) routers (assigned for the cluster head at 
each pond); and (3) coordinator (for base station node). Figure 
2 shows the structure of the Mesh network deployed in our 
proposed design. 
One of the primary benefIts of the MESH architecture is 
that if an intermediate device fails, or goes offline, or is busy, 
the information can still be transmitted or received through the 
alternative path. In the MESH architecture, the in-network 
nodes are automatically routed to fInd the most effIcient path 
for transmission in order to avoid packet drops. This is why, 
MESH architecture is usually referred to as "self-healing" and 
this is also the reason we chose MESH topology for data 
transmission in the proposed system. 
(;.---
-.. 
Fig. 3. Sensor end node hardware block diagram 
B. 
Hardware Design 
The hardware implemented in this project includes four 
parts: (1) sensor end node platform; (2) control end node 
platform; (3) cluster head platform; (4) management node 
platform. 
1) 
The sensor end node platform 
The entire sensor end node platform mainly contains of a 
microcontroller, a radio chip, and a set of sensors as shown in 
Figure 3. Each node may have a rechargeable battery with the 
solar panel as its source supply. This solar panel produces the 
required voltage and recharges the battery. 
Our sensor node platform was developed and implemented 
with consideration to low-power consumption requirements. 
Therefore, each node platform consists of a MSP430G2553 
microcontroller 
[12] which is a 16-bit ultra-low power 
microcontroller, with 16KB of internal flash, 512B RAM, 10-
bit ADC, and 1 USART. A CC2530 second generation ZigBee 
[3] solution, which can be used to develop wireless sensor 
network (WSN) applications and protocols is used as the 
transceiver. The MSP430G2553 and CC2530 combination 
provides a low-power and low-cost solution for our project. In 
this module, CC2530 and MSP430 communicate with each 
other via a serial port. 
The sensor module is used for data acquisition offering 
three 
basic 
environmental 
sensing 
parameters 
including 
temperature, pH level, and level of dissolved oxygen. 
For temperature measurement, we selected I-wire digital 
temperature sensor DS18B20 made by Dallas [6]. DS18B20 
measures temperature range from -55 to + 125°C and in the 
range of -10 to +85°C, the accuracy is ±O.5°C. It is able to 
connect to any GPIO port due to its digital output capabilities. 
For pH level measurement, we found that an "Analog pH 
Meter Kit" [7] can provide us a good solution. This kit 
consists of a pH sensor circuit board and a pH probe (BNC 
connector). It provides a full range of pH measurement from 0

> H?nh ?nh/s? ?? trong trang: 3. N?i dung h?nh ???c gi? trong PDF g?c; ch? th?ch ??c ???c ?? n?m trong ph?n v?n b?n tr?n.

## Trang 4

to 
14pH. 
G:.1r-----:lI I 
Fig. 4. Control end node hardware block diagram 
It works well under a temperature range from 0 to 60°C with a 
high accuracy of ±0.1 pH. Simply connect the PH2.0 interface 
of the sensor circuit board to any analog input port of 
MSP430, we can achieve accurate data collection. 
For DO measurement, our solution is based on a dissolved 
oxygen sensor from Atlas Scientific [8]. This sensor device 
consist of the Atlas Scientific EZO class embedded D.O. 
circuit and a D.O. probe electrode. Together they offer a very 
high level of stability and accuracy. This provides a full range 
D.O. readings from 0.01 to +35.99 mg/L and the accuracy is 
up to ±0.2. This device supports two data protocols, UART 
and I2C; therefore, it is compatible with any microcontroller 
that supports one of these two protocols. It also supports low­
power applications thereby reducing the power consumption 
on this device to only 0.995 rnA at 3.3V. 
2) 
The control end node platform 
We designed the controller nodes to activate or deactivate 
the pump oxygen system in accordance with the management 
system. It can be seen from Figure 4 where the data 
acquisition module in the sensor node is replaced by a driver 
module. This driver works according to the control commands 
from the management module. The commands can be sent 
timing, or after the data on the levels of dissolved oxygen has 
been analyzed, or as the user requests. 
3) 
The cluster head platform 
Due to the large area of the typical shrimp farm, the end 
nodes, including sensor nodes and control nodes, of each pond 
are grouped into a cluster to facilitate the management of the 
data. The cluster head is built simply by combining MSP430 
with a CC2530 ZigBee node configured in Router mode. 
4) 
The management node platform 
An intelligent controller is used to manage all the 
processes that takes place of the farm by its artificial 
intelligence 
and 
sometimes 
also 
by 
getting the control 
command from the user through a LabVIEW-based graphical 
user interface, or through a GSM gateway. Many tasks are 
performed by this management node including collecting 
sensor data from the end nodes, controlling the pwnps, and 
uploading 
data 
to 
the 
Internet. 
Fig. 5. Management node hardware block diagram 
Fig. 6. User interface of the system, in which the user chooses the soil and 
crop types that cause different values to be given by the automatic 
irrigation algorithm 
The Zigbee module used is the same as what was utilized 
in the cluster head to provide the Zigbee communication 
within the constructed wireless sensor networks. It has been 
configured as a Coordinator with the same PAN ID and the 
same RF channel as the end nodes. 
C. 
Software Design 
LabVIEW was used to develop the monitoring software in 
this study. The gathered sensor data will be displayed in table 
form and waveform chart at the GUI front panel where the 
user are able to observe the data for up to 7 prior days. The 
data received will be compared with the predetermined 
threshold value to determine that these received values are 
within or out of safe range; then the system is able to give the 
appropriate warnings. Warning of any environmental factors 
will not only be displayed on and at the same time sent to the 
user's personal mobile phone. The status of the oxygen pumps 
is also displayed and this can be control manually on the GUI. 
Figure 6 shows the graphical user interface, programmed with 
LabVIEW, of the monitoring software development. 
SMS Block Design: This block was designed by exploited 
the advantages of VISA properties in LabVIEW in which the 
MSP430 and Module SIM 900A communicate with each other 
via serial port.

> H?nh ?nh/s? ?? trong trang: 4. N?i dung h?nh ???c gi? trong PDF g?c; ch? th?ch ??c ???c ?? n?m trong ph?n v?n b?n tr?n.

## Trang 5

D. 
Patch Gateways 
Currently we used Tiva C Series TM4C1294 + CC3100 
WiFi BoosterPack platfonn [11] for the hardware utilization. 
To simplify the project and reduce the time-to-market we 
decided to program our gateway platform with the power of 
Temboo [11]; therefore, the gathered sensor information is 
then easily uploaded to a Google Spreadsheet. Finally, the user 
is able to read the data from anywhere in the world through a 
number of web-based interfaces that are supported by Temboo 
to provide the ubiquitous interfaces to the shrimp farm data. 
V. CURRENT RESULTS 
A. 
Implementation and Experimental Conditions 
In order to test the performance of the monitoring and 
control system, experiments were carried out at an industrial 
shrimp farm in Bac Lieu province, which has the second 
largest area of shrimp ponds in the Mekong Delta region. 
In the experiment, a total of 23 nodes were wirelessly 
networked for monitoring and control on two shrimp farms, of 
about 4800 square meters each. There were some network 
limitations involved, but the network can support up to 
thousands of nodes. 
B. 
System Performance 
Each sensor end node has been set to receive the in-pond 
environmental factors (temperature, pH, and dissolved oxygen 
level) every 2 hours in a normal situation. If any of these 
observing conditions drops below the predefined threshold, 
the sensor node will change to a more frequent capture rate of 
once about every 10 minutes. After the system has been fully 
operational for 3 months (from July to October, 2014), we 
found the system can automatically gather environmental 
factors and provides actuation services promptly. The system 
also demonstrated the performance of monitoring where the 
system successfully trigger an automated notification message 
through SMS gateway when any of these conditions is out of 
safety range. In addition, the oxygen pump system is also 
effectively activated or deactivated in accordance with the 
message from the authorized mobile phone number. However, 
as this is a work-in-progress project, this testing time is 
insufficient to confirm the long term reliability of the system. 
VI. CONCLUSION AND FUTURE WORKS 
This method can be adapted to requests fonned in the 
design process, updating the sensor information and reflecting 
the real factors of environmental shrimp fanning. This system 
will be labor-saving for the farner and report environmental 
changes immediately, thereby enabling the farmer to prevent 
adverse consequences. This is a low cost, ease-to-use and 
flexible to implement system as it can be integrated into small 
and medium sized shrimp fanns with minimal modifications. 
Currently this system also provides many options which are 
user friendly enabling the farmer to manage all the necessary 
farming factors resulting in increased production. 
The system also has high scalability for households or 
farming businesses on a larger scale. Currently the team 
continues to test the reliability of the system in real life 
applications. 
Acknowledgment 
The authors also would like to Mr. Huynh Huu Hanh, the 
owner of the shrimp fann in Bac Lieu province who allowed 
us to implement our proposed system in his ponds. We also 
would like to give a big thank to Mr. Nghe Quoc Khai who 
has funded partially this research work. 
References 
[I] 
A. Mainwaring, J. Polastre, R. Szewczyk, and D. Culler, "Wireless 
Sensor Networks for Habitat Monitoring", Copyright 2002, Intel 
Corporation, June 2002. 
[2] 
S. Han, Y. Kang, K. Park and M. Jang. Design of Environment 
Monitoring System for Aquaculture Farms. Frontiers in the Convergence 
of Bioscience and Information Technologies (FBIT 2007), pp.889-893, 
11-13 Oct. 2007. Jeju City. Korea. 
[3] 
Texas Instruments, "A True System-on-Chip Solution for 2.4-GHz IEEE 
802.15.4 and ZigBee Applications," CC2530 datasheet, Apr. 2009 
[Revised Feb. 2011]. 
[4] 
G H. Wang, D. Estrin, and L. Girod, "Preprocessing in a Tiered Sensor 
Network for Habitat Monitoring," In EURASIP JASP Special Issue on 
Sensor Networks, 2003. 
[5] 
H. Claussen, "Adapting a Communications Network of Wireless Access 
Nodes to a Changing Environment," United States Patent, US 7299069 
B2, November 20 2007. 
[6] 
Maxim Integrated, "DS18B20 Programmable Resolution I-Wire Digital 
Thermometer", DSI8B20 datasheet, REV: 042208. 
[7] 
DFRobot, "PH meter (SKU: SENOI61)," Aug. II, 2014. [Online]. 
Available: 
http://dfrobot.com/wiki/index.php/PH_meter(SKU:_SENOI61). 
[Accessed: Nov. 2, 2014]. 
[8] 
Atlas Scientific, "EZOTM D.O. Circuit Datasheet", version 1.1. 
[9] 
My Duyen, "Bac Lieu: Shrimp farming in greenhouses," Youtube, Jul. 
24, 
2014 
[Video 
file]. 
Available: 
http://www.youtube.com/watch?v=onZt9myITtA. [Accessed: Jul. 28, 
2014]. 
[10] Chris 
Robertson, 
"Australian 
prawn 
farming 
manual: 
health 
management for profit," department of primary industries and fisheries, 
[online document], 2006. Available: Australian Centre for International 
Agricultural Research, http://aciar.gov.au/publication/copOOI [Accessed: 
Aug 1, 2014]. 
[II] Temboo. "Texas Instruments + Temboo: "Program your TI LaunchPad 
with the power of Temboo," www.temboo.com. [Online]. Available: 
https:l/www.temboo.com/hardware/ti [Accessed: Oct. OS, 2014]. 
[I 2] Texas Instruments, "Mixed Signal Microcontroller," MSP430G2x53 
datasheet, Apr. 2011 [Revised May. 2013].

> H?nh ?nh/s? ?? trong trang: 1. N?i dung h?nh ???c gi? trong PDF g?c; ch? th?ch ??c ???c ?? n?m trong ph?n v?n b?n tr?n.

