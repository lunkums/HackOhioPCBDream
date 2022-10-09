using UnityEngine;

public class Map : MonoBehaviour
{
    private SpriteRenderer spriteRenderer;

    void Awake()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
        spriteRenderer.receiveShadows = true;
        spriteRenderer.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.On;
    }
}
