from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class ImageCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    SUBCATEGORY_CHOICES = [
        # Architecture Categories
        ('residential-architecture', 'Residential Architecture'),
        ('single-family-homes', 'Single-family Homes'),
        ('multi-family-housing', 'Multi-family Housing (Apartments, Condominiums, etc.)'),
        ('villas-and-luxury-homes', 'Villas and Luxury Homes'),
        ('tiny-houses', 'Tiny Houses and Sustainable Housing'),
        ('commercial-architecture', 'Commercial Architecture'),
        ('office-buildings', 'Office Buildings'),
        ('retail-spaces', 'Retail Spaces (Shopping Malls, Storefronts, etc.)'),
        ('restaurants-and-cafes', 'Restaurants and Cafes'),
        ('mixed-use-developments', 'Mixed-use Developments'),
        ('industrial-architecture', 'Industrial Architecture'),
        ('factories', 'Factories'),
        ('warehouses', 'Warehouses'),
        ('power-plants', 'Power Plants'),
        ('data-centers', 'Data Centers'),
        ('institutional-architecture', 'Institutional Architecture'),
        ('schools-and-universities', 'Schools and Universities'),
        ('hospitals-and-healthcare', 'Hospitals and Healthcare Facilities'),
        ('libraries', 'Libraries'),
        ('museums-and-cultural-centers', 'Museums and Cultural Centers'),
        ('landscape-architecture', 'Landscape Architecture'),
        ('parks-and-recreational-areas', 'Parks and Recreational Areas'),
        ('urban-green-spaces', 'Urban Green Spaces'),
        ('gardens-and-terraces', 'Gardens and Terraces'),
        ('sustainable-landscapes', 'Sustainable Landscapes'),
        ('urban-planning', 'Urban Planning and Design'),
        ('city-planning', 'City Planning'),
        ('infrastructure-projects', 'Infrastructure Projects'),
        ('transportation-hubs', 'Transportation Hubs (Bus/Train Stations, Airports)'),
        ('zoning-and-land-use', 'Zoning and Land-use Planning'),
        ('interior-architecture', 'Interior Architecture and Design'),
        ('residential-interiors', 'Residential Interiors'),
        ('commercial-interiors', 'Commercial Interiors (Offices, Retail, etc.)'),
        ('hospitality-interiors', 'Hospitality Interiors (Hotels, Resorts, etc.)'),
        ('furniture-design', 'Furniture and Fixture Design'),
        ('sustainable-design', 'Sustainable and Green Design'),
        ('passive-solar-design', 'Passive Solar Design'),
        ('leed-certified-buildings', 'LEED-certified Buildings'),
        ('renewable-energy-integration', 'Renewable Energy Integration'),
        ('energy-efficient-buildings', 'Energy-efficient Buildings'),
        ('cultural-and-religious-architecture', 'Cultural and Religious Architecture'),
        ('religious-structures', 'Churches, Mosques, Temples, and Synagogues'),
        ('performing-arts-centers', 'Theaters and Performing Arts Centers'),
        ('heritage-preservation', 'Heritage and Preservation Projects'),
        ('specialized-architecture', 'Specialized Architecture'),
        ('sports-facilities', 'Sports Facilities and Stadiums'),
        ('convention-centers', 'Convention Centers'),
        ('amusement-parks', 'Amusement Parks'),
        ('aquariums-and-zoos', 'Aquariums and Zoos'),

        # Construction Management Categories
        ('pre-construction', 'Pre-construction Design'),
        ('feasibility-studies', 'Feasibility Studies'),
        ('cost-estimation', 'Cost Estimation'),
        ('scheduling-and-planning', 'Scheduling and Planning'),
        ('risk-management', 'Risk Management Plans'),
        ('structural-design', 'Structural Design'),
        ('foundation-systems', 'Foundation Systems'),
        ('load-bearing-structures', 'Load-bearing Structures'),
        ('bridges-and-tunnels', 'Bridges and Tunnels'),
        ('high-rise-frameworks', 'High-rise Building Frameworks'),
        ('mep-design', 'Mechanical, Electrical, and Plumbing (MEP) Design'),
        ('hvac-systems', 'HVAC Systems'),
        ('plumbing-drainage-systems', 'Plumbing and Drainage Systems'),
        ('electrical-lighting-systems', 'Electrical Wiring and Lighting Systems'),
        ('fire-protection-systems', 'Fire Protection Systems'),
        ('civil-engineering-design', 'Civil Engineering Design'),
        ('road-highway-construction', 'Road and Highway Construction'),
        ('drainage-systems', 'Drainage Systems'),
        ('land-development', 'Land Development'),
        ('water-supply-systems', 'Water Supply Systems'),
        ('project-management', 'Project Management Design'),
        ('construction-logistics', 'Construction Logistics'),
        ('site-safety-plans', 'Site Safety Plans'),
        ('material-procurement-plans', 'Material Procurement Plans'),
        ('quality-control-measures', 'Quality Control Measures'),
        ('facade-roofing-design', 'Facade and Roofing Design'),
        ('curtain-wall-systems', 'Curtain Wall Systems'),
        ('energy-efficient-facades', 'Energy-efficient Facades'),
        ('green-roofs', 'Green Roofs'),
        ('skylights-atriums', 'Skylights and Atriums'),
        ('construction-technology', 'Construction Technology and Innovation'),
        ('bim', 'BIM (Building Information Modeling)'),
        ('prefabrication', 'Prefabrication and Modular Construction'),
        ('smart-building-systems', 'Smart Building Systems'),
        ('construction-robotics', 'Robotics and Automation in Construction'),
        ('sustainability-environmental-design', 'Sustainability and Environmental Design'),
        ('energy-efficient-materials', 'Energy-efficient Materials'),
        ('waste-management-strategies', 'Waste Management Strategies'),
        ('renewable-energy-construction', 'Renewable Energy Integration'),
        ('water-conservation-systems', 'Water Conservation Systems'),
        ('post-construction', 'Post-construction and Maintenance Design'),
        ('facility-management-systems', 'Facility Management Systems'),
        ('retrofitting-renovation', 'Retrofitting and Renovation'),
        ('maintenance-schedules', 'Maintenance Schedules'),
        ('asset-management', 'Asset Management'),
        ('disaster-resilient-design', 'Disaster-Resilient Design'),
        ('earthquake-resistant-buildings', 'Earthquake-resistant Buildings'),
        ('flood-protection-systems', 'Flood Protection Systems'),
        ('wind-resistant-designs', 'Wind and Hurricane-resistant Designs'),
        ('fire-safety-evacuation', 'Fire Safety and Evacuation Plans'),

        # Overlapping and Emerging Categories
        ('smart-city-design', 'Smart City Design'),
        ('iot-integration', 'IoT Integration'),
        ('digital-twin-modeling', 'Digital Twin Modeling'),
        ('smart-transportation-systems', 'Smart Transportation Systems'),
        ('heritage-conservation', 'Cultural Heritage and Conservation'),
        ('historic-building-restoration', 'Restoration of Historic Buildings'),
        ('adaptive-reuse', 'Adaptive Reuse of Old Structures'),
        ('healthcare-wellness-design', 'Healthcare and Wellness Design'),
        ('healing-environments', 'Healing Environments'),
        ('biophilic-design', 'Biophilic Design'),
        ('aging-in-place-housing', 'Aging-in-place Housing'),
        ('transportation-design', 'Transportation Design'),
        ('airports-seaports', 'Airports and Seaports'),
        ('bus-train-stations', 'Bus and Train Stations'),
        ('parking-structures', 'Parking Structures'),
        ('mixed-use-design', 'Mixed-use Development Design'),
        ('parametric-design', 'Parametric and Computational Design'),
        ('algorithm-driven-architecture', 'Algorithm-driven Architecture'),
        ('generative-design', 'Generative Design Processes'),
    ]

    
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, default='Title',blank=True,null=True )
    description = models.TextField(blank=True,null=True )
    location = models.CharField(max_length=100, default='Location')
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)  # Primary category
    subcategory = models.CharField(
        max_length=100, 
        choices=SUBCATEGORY_CHOICES, 
        default='others',
        blank=True,  # Allow blank in forms
        null=True     # Allow NULL value in the database
    )
    
    name = models.CharField(max_length=100, default='Name',blank=True, null=True )  
    role = models.CharField(max_length=100, default='Role',blank=True, null=True )
    posted_date = models.DateTimeField(default=now)
    magazine_type = models.CharField(max_length=100, default='Architectural magazine',blank=True,null=True )
    service_title = models.CharField(max_length=100, default='Architectural and construction service',blank=True,null=True ) 
    service_Description = models.TextField(blank=True,null=True )

    def clean(self):
        if self.posted_date > now():
            raise ValidationError("Posted date cannot be in the future.")

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Services(models.Model):
    service_title = models.CharField(max_length=150, default="Default Service Title")  # Default title
    image = models.ImageField(upload_to='images/',blank=True,null=True)  # Default image path
    description = models.TextField(default="this services is provided by Fact ltd, which is located in Kigali.") 
    

    def __str__(self):
        return self.service_title

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/') # Upload path for videos
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title