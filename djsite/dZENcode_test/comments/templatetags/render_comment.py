from django import template
register = template.Library()


def render_comment(comment):
    return f"""
        <li>
            <h3>{ comment.user.name } { comment.datetime.strftime('%d.%m.%Y в %H:%M') }</h3>
            <p>{ comment.text }</p>
            <button id="comment_id" class="open-popup" type="submit" value={ comment.id }>Відповісти</button>
        </li>
        """


@register.filter
def render_comments(comments):
    res = "<ul>"
    for comment in comments:
        res += render_comment(comment)
        children_comments = comment.children_comments
        if children_comments:
            res += f"<ul> {render_comments(children_comments)} </ul>"
    res += "</ul>"
    return res
