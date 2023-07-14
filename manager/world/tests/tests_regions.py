from django.test import TestCase, Client
from faker import Faker
from world.models import Regions

fake = Faker()
client = Client()


class RegionsCreationTest(TestCase):
    def test_regions_creation_with_name(self):
        Regions.objects.create(
            name="Olïzya",
        )
        region = Regions.objects.get(name="Olïzya")
        assert region.name == "Olïzya"
        assert region.visited == False
        assert region.religion == None
        assert region.politic == None
        assert region.chief == None
        assert region.region_maps_url == None
        assert region.description == None
        assert region.history_in_campaign == None
    
    def test_regions_creation_with_name_and_request(self):
        region = {
            "name": "Muick",
        }
        response = client.post("/world/create-region", region)
        assert not response.status_code == 404
        new_region = Regions.objects.get(name="Muick")
        assert new_region.name == "Muick"
        assert new_region.visited == False
        assert new_region.religion == None
        assert new_region.politic == None
        assert new_region.chief == None
        assert new_region.region_maps_url == None
        assert new_region.description == ''
        assert new_region.history_in_campaign == ''


class RegionsUpdateTest(TestCase):
    def setUp(self) -> None:
        Regions.objects.create(
            name="Olïzya",
        )

    def test_regions_update(self):
        region = Regions.objects.get(name="Olïzya")
        assert (
            region.name == "Olïzya"
            and region.visited == False
            and region.religion == None
            and region.politic == None
            and region.chief == None
            and region.region_maps_url == None
            and region.description == None
        )
        fake_region_description = fake.sentence()

        region.visited = True
        region.religion = "Lalante"
        region.politic = "Matronnie"
        region.chief = "Toad"
        region.region_maps_url = "https://www.aidedd.org/atlas/index.php?map=P&l=0"
        region.description = fake_region_description

        region.save()

        update_region = Regions.objects.get(name="Olïzya")
        assert update_region.name == "Olïzya"
        assert update_region.visited == True
        assert update_region.religion == "Lalante"
        assert update_region.politic == "Matronnie"
        assert update_region.chief == "Toad"
        assert (
            update_region.region_maps_url == "https://www.aidedd.org/atlas/index.php?map=P&l=0"
        )
        assert update_region.description == fake_region_description
        assert region.history_in_campaign == None
