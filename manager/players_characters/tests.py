from django.test import TestCase, Client
from faker import Faker
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.pdf_file.generators.pdfkit_generator import PdfkitPdfGenerator

from players_characters.models import PlayersCharacters

fake = Faker()
fake.add_provider(PdfFileProvider)
client = Client()


class CreatePlayersCharacters(TestCase):
    def test_i_should_create_a_players_character(self) -> None:
        PlayersCharacters.objects.create(name="Shinji")

        character = PlayersCharacters.objects.get(name="Shinji")
        assert character

    def test_i_should_create_a_players_character_player(self) -> None:
        PlayersCharacters.objects.create(name="Rei", player="Jean-Jacques")

        character = PlayersCharacters.objects.get(name="Rei")
        assert character
        assert character.player == "Jean-Jacques", "Player field failed"

    def test_i_should_create_a_players_character_cs_url(self) -> None:
        PlayersCharacters.objects.create(
            name="Azuka",
            character_sheet_url="https://evangelion.fandom.com/wiki/Asuka_Langley_Sohryu",
        )

        character = PlayersCharacters.objects.get(name="Azuka")
        assert character
        assert (
            character.character_sheet_url
            == "https://evangelion.fandom.com/wiki/Asuka_Langley_Sohryu"
        ), "Url character Fail"

    # def test_i_should_create_a_players_character_cs_file(self) -> None:
    #     sheet_file = fake.pdf_file(pdf_generator_cls=PdfkitPdfGenerator)
    #     PlayersCharacters.objects.create(name="Misato", character_sheet_file=sheet_file)
    #     character = PlayersCharacters.objects.get(name="Misato")
    #     assert character
    #     assert character.character_sheet_file

    def test_i_should_create_cs_with_request(self) -> None:
        # sheet_file = fake.pdf_file(pdf_generator_cls=PdfkitPdfGenerator)
        character = {
            "name": "Eva001",
            "player": "Pierre",
            "character_sheet_url": "https://evangelion.fandom.com/wiki/Asuka_Langley_Sohryu",
            # "character_sheet_file": sheet_file,
        }
        response = client.post("/characters/create", character)
        assert not response.status_code == 404
        new_character = PlayersCharacters.objects.get(name='Eva001')
        assert new_character.name == "Eva001" and new_character.player == "Pierre"


class UpdatePlayersCharacters(TestCase):
    def setUp(self) -> None:
        PlayersCharacters.objects.create(
            name="Shinji",
        )

    def test_i_should_update_a_character(self) -> None:
        character = PlayersCharacters.objects.get(name="Shinji")
        assert character
        assert character.name == "Shinji"

        character.player = "Pierre"
        character.save()

        update_character = PlayersCharacters.objects.get(name="Shinji")
        assert update_character
        assert update_character.name == "Shinji" and update_character.player == "Pierre"

    def test_i_should_update_a_character_with_request(self) -> None:
        character = PlayersCharacters.objects.get(name="Shinji")
        assert character
        assert character.name == "Shinji"
        assert not character.player

        update = {
            "name": character.name,
            "player": "Pierre",
            "character_sheet_url": "",
            # "character_sheet_file": sheet_file,
        }
        response = client.post(f"/characters/update/{character.pk}", update)
        assert not response.status_code == 404, f"response = {response.status_code}"
        update_character = PlayersCharacters.objects.get(name="Shinji")
        assert update_character.name == "Shinji" 
        assert update_character.player == "Pierre"


class DeletePlayersCharacters(TestCase):
    def setUp(self) -> None:
        PlayersCharacters.objects.create(
            name="Shinji",
        )

    def test_i_should_delete_a_character(self) -> None:
        character = PlayersCharacters.objects.get(name="Shinji")
        assert character
        assert character.name == "Shinji"

        character.delete()

        character = PlayersCharacters.objects.filter(name="Shinji")
        assert not character
