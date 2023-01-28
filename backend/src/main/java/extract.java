import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Main {
    public static void main(String[] args) throws Exception {

        // Replace this with the address you want to search
        String address = "";

        // Scraping Uber Eats
        String url = "https://www.ubereats.com/en-US/search/"+address+"/";
        Document document = Jsoup.connect(url).get();
        Elements cards = document.select(".c-search-card");
        System.out.println("Uber Eats:");
        for (Element card : cards) {
            String restaurantName = card.select(".c-search-card__name").text();
            String deliveryTime = card.select(".c-search-card__delivery-time").text();
            String priceRange = card.select(".c-search-card__price-range").text();
            System.out.println("Restaurant: " + restaurantName);
            System.out.println("Delivery Time: " + deliveryTime);
            System.out.println("Price Range: " + priceRange);
            System.out.println();
        }

        // Scraping Doordash
        url = "https://www.doordash.com/en-US/search/"+address+"/";
        document = Jsoup.connect(url).get();
        cards = document.select(".c-search-card");
        System.out.println("Doordash:");
        for (Element card : cards) {
            String restaurantName = card.select(".c-search-card__name").text();
            String deliveryTime = card.select(".c-search-card__delivery-time").text();
            String priceRange = card.select(".c-search-card__price-range").text();
            System.out.println("Restaurant: " + restaurantName);
            System.out.println("Delivery Time: " + deliveryTime);
            System.out.println("Price Range: " + priceRange);
            System.out.println();
        }

        // Scraping Raddish
        url = "https://www.raddish.com/en-US/search/"+address+"/";
        document = Jsoup.connect(url).get();
        cards = document.select(".c-search-card");
        System.out.println("Raddish:");
        for (Element card : cards) {
            String restaurantName = card.select(".c-search-card__name").text();
            String deliveryTime = card.select(".c-search-card__delivery-time").text();
            String priceRange = card.select(".c-search-card__price-range").text();
            System.out.println("Restaurant: " + restaurantName);
            System.out.println("Delivery Time: " + deliveryTime);
            System.out.println("Price Range: " + priceRange);
            System.out.println();
        }
    }
}
