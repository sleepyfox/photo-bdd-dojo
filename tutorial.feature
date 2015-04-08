Feature: share a photo
  As a photographer
  I want to take pictures
  So that all my friends can see what an amazing life I have

  Scenario: publish a photo
      Given that I'm logged in
      When I take an amazing photo
      And approve it (obviously)
      Then I should be able to see it on my photo stream

Feature: browse friend's photos
  As a friend of a photographer
  I want to see my friends' amazing photos
  So that I can dream of going to Bali one day

  Scenario: browse
      Given that my friend Bob has taken several pictures
      When I view his photo stream
      Then I should see his latest approved photo first
      And then let you scroll through them vertically
