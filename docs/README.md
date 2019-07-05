# Daylight 0.1 Description

# Vision

The first limited public release of daylight should provide a smooth, familiar
dating application experience with some core features to cater to trans women
and feminine-identifying, non-binary and gender non-conforming individuals
looking to date men and masc-identifying individuals and/or each other.  In
other words, this version of daylight will unfortunately make a crude
distinction between members of its user-base.  While dramatically over-
simplifying the complex distinctions between different users, this
simplification will enable daylight to deliver on its promise to provide a
dating experience that directly challenges some big problems on
conventional dating sites.

First, daylight is designed and should always retain its values of respecting
its users, their privacy and their trust equally.

Second, daylight distinctly privileges its broader category of users, those
identifying as trans women / trans feminine, femmes, non-binary and gender
non-conforming individuals over men and masculine-identifying individuals
(trans or cis).

    * In order to relieve the problem of inboxes being flooded
    with unwanted messages, daylight will only allow one-way likes before a
    match is established.
    * Match queues will prevent or else slow down indiscriminate liking of
    other users.
    * A one-sided reputation system will silently bias match-finding in
    favour of men and mascs that feature a few qualities essential to being
    respectful specifically to the rest of the user-base but no more.
    * A simple match recommendation system that scores match candidacy by
    reputation, tag matches and contact recency with no learning system to
    quantify trends in user behaviour or tag compatibility.

Ideally, daylight would encourage men and mascs to become educated about the
specific dating pool they are tapping into, to be respectful and to be
supportive.  The fact that this system is in place must be transparent first
and foremost but daylight should also do some of the work to disseminate
knowledge and advice by linking to resources and communities that can help.

In future releases of daylight, greater support for more diverse experiences is
the primary goal.  Along with making the site more functional, performant and
usable, daylight should evolve to better accomodate the specific needs of all
of its users.  However, in believing in the value of diverse ecosystems of
software, it should be considered that it may be best for daylight to only
attempt to provide a specific experience.

# Features

The first usable version of daylight should provide a functional dating site
experience.  This should include the bare minimum of:

    1. Creating a profile with interest tags and a bio.
    2. Uploading photos.
    3. Finding and expressing interest in people.
    4. Chatting with matches.
    5. Maintaining a list of contacts.

These features will cover the core of the experience.  However at this point,
daylight would not have any features that make it stand out from any other
dating site.  In order to really deliver on its promise, the first release of
daylight should accomodate the following experiences:

    1. Experience ratings given only by and visible only to women and femmes.
    2. Match queues limit every user to X expiring matches at a time.

Features that may be worth exploring but will _not_ be implemented for the 0.1
release:

    1. A chat bot to interview men / mascs and display answers to women and
    femmes.
    2. A sophisticated matching algorithm.
    3. Greater consideration for non-binary and gender-nonconforming
    experiences.

At this stage of development, some thing are simply not going to be a priority.
That will include things like scaling and appealing to the broadest possible
audience.  At no point should monetization even be considered.

## Feature 1: User Profiles

Each user has a profile page that includes:

    * The name they use.
    * Their pronouns.
    * A biography giving plenty of room to write.
    * A profile photo to use in thumbnails.
    * Tags that describe their interests.

## Feature 2: Photo Uploading

Users should be able to upload photos of a limited size to be displayed in
their profiles.

## Feature 3: Finding and Liking Other Users

One page should be dedicated to listing users that may be a good match
according to a simple reccommendation system that does not learn.

## Feature 4: Match Chats

Once users establish matches with other users by both users sending a like to
one another, those users should be able to have text chats.  It may be best to
offload the work of handling chats to another service such as Matrix.

## Feature 5: Contact Lists

See **Special Feature 2**.  Once a match expires from a user's match queue,
an opportunity to add the match to a contacts list should be presented.

## Special Feature 1: One-Sided Experience Ratings

After a match expires, trans women and femmes should be given the option to
rate their experience with the match if and only if the match was a man or
masc.  These requests will only allow for simple one (1) to five (5) star
rating.  The message to users should be that the rating should represent the
match's respectfulness, support and familiarity with their experience.  These
ratings must be collected anonymously and aggregated.

Because this feature creates an explicit inequality between users, the
influence of reputation on match recommendations should be very clear and easy
to adjust.

## Special Feature 2: Match Queues

Once two users match by sending a like to each other, they will be able to chat
freely for a limited time.  During that time, the two parties should make plans
to communicate off the daylight platform.  By tightly limitng the number of
matches users can maintain at a time, we encourage users to make plans to stay
in touch or set up dates.  We also encourage users to spend less time on the
site and more time trying to make connections.  Hopefully, this restriction
will also make it impossible to indiscriminately like other users and annoy or
harass.
